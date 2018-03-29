<HTML>

	<HEAD>

		<TITLE>epimaps

		</TITLE>

		<link rel="shortcut icon" href="favicon.ico" type="image/vnd.microsoft.icon">		

	</HEAD>

	<BODY bgColor=#7f7f7f>

		<?

			function getLatLng($address)
			{
				$address=plusSpace($address);
				$uri="http://maps.google.com/maps/geo?q=".$address."&output=csv&key=ABQIAAAAWGKa8_PMIMNcsIeNnJalZxRlWRzoYO-H72wyf2v4NCndZHa7kBT_o61pbYGrZ5yju1tmrzLLrdiVmg";
				$wtf=file_get_contents($uri,r);

				$rus=explode(",",$wtf);

				return $rus;
			}

		?>

<form name="input" action="map.php" method="get">
1: 
<input type="text" name="loc1">
2:
<input type="text" name="loc2">
3:
<input type="text" name="loc3">
<input type="submit" value="Submit">
</form>

		<?

			function plusSpace($address)
			{
				return strtr($address," ","+");
			}

		?>

	</BODY>

</HTML>