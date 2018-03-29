<html>
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8"/>

		<title>epimaps</title>

		<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAWGKa8_PMIMNcsIeNnJalZxRlWRzoYO-H72wyf2v4NCndZHa7kBT_o61pbYGrZ5yju1tmrzLLrdiVmg"type="text/javascript">
		</script>

		<script type="text/javascript">
			//<![CDATA[
				function load() {
					if (GBrowserIsCompatible()) {
						var map;
						var directionsPanel;
						var directions;
						map = new GMap2(document.getElementById("map"));
						directionsPanel = document.getElementById("my_textual_div");
						map.setCenter(new GLatLng(49.496675,-102.65625), 5);
						directions = new GDirections(map, directionsPanel);
						directions.load("Kettering,OH to St. Louis, MO");
					}
   		  		 }
			//]]>
		</script>

  	</head>

	<body onload="load()" onunload="GUnload()">

		<div id="map" style="width: 800px; height: 800px"></div>

	</body>
</html>