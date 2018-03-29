<HTML>

	<HEAD>

		<TITLE>epimaps

		</TITLE>

		<link rel="shortcut icon" href="favicon.ico" type="image/vnd.microsoft.icon">		

	</HEAD>

	<BODY bgColor=#7f7f7f>

		<?		
		
			function getTime($near,$far)
			{
				$A=plusSpace($near);
				$B=plusSpace($far);
				$uri="http://maps.google.com/maps?q=from+".$A."+to+".$B."&output=kml";
				$wtf=file_get_contents($uri,r);

				$rus=explode("><",$wtf);
				$ygbsm=array_filter($rus,"cdataFilter");
				$the_one=array_keys($ygbsm);
				$the_key=count($the_one)-1;
				$the_element=$ygbsm[$the_one[$the_key]];
				$the_element_front=explode(")<br/>",$the_element);
				$the_element_center=explode("(about ",$the_element_front[0]);
				$the_time=$the_element_center[1];
				$the_time_array=explode(" ",$the_time);
				$minutes=0;
				for ($counter=0; $counter<count($the_time_array)/2; $counter++)
				{
					if (substr($the_time_array[$counter*2+1],0,1) == "d")
						$minutes += $the_time_array[$counter*2]*24*60;
					elseif (substr($the_time_array[$counter*2+1],0,1) == "h")
						$minutes += $the_time_array[$counter*2]*60;
					elseif (substr($the_time_array[$counter*2+1],0,1) == "m")
						$minutes += $the_time_array[$counter*2];
				}
				return $minutes;
			}
			
			function cdataFilter($value)
			{
				if (substr($value,0,8)=="![CDATA[")
				{
					return true;
				}
				return false;
			}


			function plusSpace($address)
			{
				return strtr($address," ","+");
			}

			function getAddressArray()
			{
				$the_array=array(array(array("Origin"),array($_POST["Origin"])));
				for ($counter=1; $counter <= $_POST["groups"]; $counter++)
				{
					$the_array[$counter]=array(array($_POST["Group_".$counter."_Label"]));
					for ($count=1; $count <= $_POST["Group_".$counter."_Members"]; $count++)
						$the_array[$counter][$count]=array($_POST["Group_".$counter."_Stop_".$count."_Address"]);
				}
				if ($_POST["type"]=="One Way")
					$the_array[$_POST["groups"]+1]=array(array("Destination"),array($_POST["Destination"]));
				else
					$the_array[$_POST["groups"]+1]=array(array("Destination"),array($_POST["Origin"]));
				return $the_array;
			}

			function getGroupsDistance($higher_group,$lower_group,$addresses)
			{
				$groups_distance_array=array();
				for ($counter = 1; $counter < count($addresses[$higher_group]); $counter++)
					for ($count = 1; $count < count($addresses[$lower_group]); $count++)
						$groups_distance_array[$counter][$count]=getTime($addresses[$higher_group][$counter][0],$addresses[$lower_group][$count][0]);
				return $groups_distance_array;
			}

			function getAllGroupsDistance($addresses)
			{
				$groups_metadistance_array=array(array());
				for ($counter=0; $counter < count($addresses)-1; $counter++)
					for ($count=1; $count < count($addresses); $count++)
						if ($counter != $count && ($counter != 0 || $count != count($addresses)-1))
							$groups_metadistance_array[$counter][$count]=getGroupsDistance($counter,$count,$addresses);
			return $groups_metadistance_array;
			}

			function getMetapathArray($legs,$metapath_array,$metapath,$stops,$count)
			{
				for ($counter = 1; $counter <= $stops; $counter++)
				{
					if ($stops >= $count && in_array($counter,$metapath) != 1)
					{
						$metapath[$count]=$counter;
						if ($stops > $count)
							$metapath_array[$counter]=getMetapathArray($legs,$metapath_array[$counter],$metapath,$stops,$count+1);
						elseif ($stops = $count)
						{
							$metapath[0]=0;
							ksort($metapath);
							$metapath[count($metapath)]=count($metapath);
							$metapath_array[$counter]=getMetapathDistances($legs,$metapath,$stops,array(),0,1,0);
						}
					}
				}
				return $metapath_array;
			}

			function getMetapathDistances($legs,$metapath,$stops,$metapath_distance_array,$count,$whichone,$length)
			{
				for ($counter = 1; $counter <= count($legs[$metapath[$count]][$metapath[$count+1]][$whichone]); $counter++)
				{
					if ($count < $stops)
					{
						$metapath_distance_array[$counter]=getMetapathDistances($legs,$metapath,$stops,$metapath_distance_array[$counter],$count+1,$counter,$length+$legs[$metapath[$count]][$metapath[$count+1]][$whichone][$counter]);
					}
					else
					{
						$metapath_distance_array[$counter]=$length+$legs[$metapath[$count]][$metapath[$count+1]][$whichone][$counter];
					}
				}
				return $metapath_distance_array;
			}
			
			function routeString($addresses,$pathstring)
			{
				$path_array=explode(":",$pathstring);
				array_shift($path_array);
				for ($counter = 0; $counter < count($path_array)/2; $counter++)
					$stops_array[$counter]=array($path_array[$counter],$path_array[$counter+count($path_array)/2]);
				$stops=count($addresses)-2;
				$the_string = "from: ".$addresses[0][1][0];
				for ($counter = 0; $counter < $stops; $counter++)
				{
					$the_string = $the_string." to: ".$addresses[$stops_array[$counter][0]][$stops_array[$counter][1]][0];
				}
				$the_string = $the_string." to: ".$addresses[$stops+1][1][0];
				return $the_string;
			}
			
			function getFastestRoute($metapath_array,$stuff_array)
			{
			$minvalue=$stuff_array[0];
			$pathstring=$stuff_array[1];
				foreach ($metapath_array as $which => $thingies)
				{
					if (is_array($thingies))
					{
						$smartmouth = getFastestRoute($thingies,array($minvalue,$pathstring.":".$which));
						if ($smartmouth[0] < $minvalue)
						{
							$minvalue = $smartmouth[0];
							$PS=$smartmouth[1];
						}
					}
					elseif ($minvalue > $thingies)
					{
						$minvalue = $thingies;
						$PS=$pathstring;
					}
				}
				return array($minvalue,$PS);
			}

		?>

		<?
			set_time_limit(0);
			$address_array=getAddressArray();
			$metapaths=getMetapathArray(getAllGroupsDistance($address_array),array(),array(),count($address_array)-2,1);
			$shortestpath=getFastestRoute($metapaths,array(1000000,""));
			$the_best_route=routeString($address_array,$shortestpath[1]);
		?>

<form name="myform" action="epimaps.htm">
</form>
		
		<SCRIPT language="JavaScript">
		
		<?
echo("firstVar = '".$the_best_route."';");
?>

function setCookie(c_name,value,expiredays)
{
var exdate=new Date();
exdate.setDate(exdate.getDate()+expiredays);
document.cookie=c_name+ "=" +escape(value)+
((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
}

setCookie("whereto",firstVar,1);

document.myform.submit(); //Reinstate this line to test its passing to epimaps.htm

</SCRIPT>

	</BODY>

</HTML>