<? session_start(); ?>

<HTML>

	<HEAD>

		<TITLE>epimaps

		</TITLE>

		<link rel="shortcut icon" href="favicon.ico" type="image/vnd.microsoft.icon">		

	</HEAD>

	<BODY bgColor=#7f7f7f>

		<?
			function getDistance($lat1, $long1, $lat2, $long2)
			{
				$earth = 3963.1; //miles

				//Point 1 cords
				$lat1 = deg2rad($lat1);
				$long1= deg2rad($long1);

				//Point 2 cords
				$lat2 = deg2rad($lat2);
				$long2= deg2rad($long2);

				//Haversine Formula
				$dlong=$long2-$long1;
				$dlat=$lat2-$lat1;

				$sinlat=sin($dlat/2);
				$sinlong=sin($dlong/2);

				$a=($sinlat*$sinlat)+cos($lat1)*cos($lat2)*($sinlong*$sinlong);

				$c=2*asin(min(1,sqrt($a)));

				$d=$earth*$c;

				return $d;
			}

			function getLatLng($address)
			{
				$address=plusSpace($address);
				$wtf=file_get_contents("http://maps.google.com/maps/geo?q=".$address."&output=csv&key=ABQIAAAAWGKa8_PMIMNcsIeNnJalZxRlWRzoYO-H72wyf2v4NCndZHa7kBT_o61pbYGrZ5yju1tmrzLLrdiVmg",r);
				$rus=explode(",",$wtf);
				return $rus;
			}

			function plusSpace($address)
			{
				return strtr($address," ","+");
			}

			function getAddressArray()
			{
				$LatLng=getLatLng($_POST["Origin"]);
				$Lat=$LatLng[2];
				$Lng=$LatLng[3];
				$the_array=array(array(array("Origin"),array($_POST["Origin"],$Lat,$Lng)));
				for ($counter=1; $counter <= $_POST["groups"]; $counter++)
				{
					$the_array[$counter]=array(array($_POST["Group_".$counter."_Label"]));
					for ($count=1; $count <= $_POST["Group_".$counter."_Members"]; $count++)
					{
						$LatLng=getLatLng($_POST["Group_".$counter."_Stop_".$count."_Address"]);
						$Lat=$LatLng[2];
						$Lng=$LatLng[3];
						$the_array[$counter][$count]=array($_POST["Group_".$counter."_Stop_".$count."_Address"],$Lat,$Lng);
					}
				}
				if ($_POST["type"]=="One Way")
				{
					$LatLng=getLatLng($_POST["Destination"]);
					$Lat=$LatLng[2];
					$Lng=$LatLng[3];
					$the_array[$_POST["groups"]+1]=array(array("Destination"),array($_POST["Destination"],$Lat,$Lng));
				}
				else
				{
					$LatLng=getLatLng($_POST["Origin"]);
					$Lat=$LatLng[2];
					$Lng=$LatLng[3];
					$the_array[$_POST["groups"]+1]=array(array("Destination"),array($_POST["Origin"],$Lat,$Lng));
				}
				return $the_array;
			}

			function getGroupsDistance($higher_group,$lower_group,$addresses)
			{
				$groups_distance_array=array();
				for ($counter = 1; $counter < count($addresses[$higher_group]); $counter++)
				{
					for ($count = 1; $count < count($addresses[$lower_group]); $count++)
					{
						$groups_distance_array[$counter][$count]=getDistance($addresses[$higher_group][$counter][1],$addresses[$higher_group][$counter][2],$addresses[$lower_group][$count][1],$addresses[$lower_group][$count][2])."<br/>";
					}
				}
				return $groups_distance_array;
			}

			function getAllGroupsDistance($addresses)
			{
				$groups_metadistance_array=array(array());
				for ($counter=0; $counter < count($addresses)-1; $counter++)
				{
					for ($count=1; $count < count($addresses); $count++)
					{
						if ($counter != $count && ($counter != 0 || $count != count($addresses)-1))
							$groups_metadistance_array[$counter][$count]=getGroupsDistance($counter,$count,$addresses);
					}
				}
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

		?>

		<?
			set_time_limit(0);
			$address_array=getAddressArray();
			$leg_array=getAllGroupsDistance($address_array);
			$metapaths=getMetapathArray($leg_array,array(),array(),count($address_array)-2,1);
			print_r($metapaths);
		?>

	</BODY>

</HTML>