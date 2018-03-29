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

		?>

<form name="input" action="#" method="post">
Start: 
<input type="text" name="loc1">
Finish:
<input type="text" name="loc2">
<input type="submit" value="Submit">
</form>

		<?

			function plusSpace($address)
			{
				return strtr($address," ","+");
			}

		?>

		<?
			$LatLng1=getLatLng($_POST["loc1"]);
			$Lat1=$LatLng1[2];
			$Lng1=$LatLng1[3];
			$LatLng2=getLatLng($_POST["loc2"]);
			$Lat2=$LatLng2[2];
			$Lng2=$LatLng2[3];
			echo "Distance in miles: ".getDistance($Lat1, $Lng1, $Lat2, $Lng2)."<br/>";
			echo plusSpace($_POST["loc1"])."<br/>";
			echo $Lat1."<br/>";
			echo $Lng1."<br/>";
			echo plusSpace($_POST["loc2"])."<br/>";
			echo $Lat2."<br/>";
			echo $Lng2."<br/>";

		?>

	</BODY>

</HTML>