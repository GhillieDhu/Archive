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

		<?

			function plusSpace($address)
			{
				return strtr($address," ","+");
			}

		?>
		
		
		
<SCRIPT language="JavaScript">

	  window.location.get = new Object();
	  if (window.location.search && window.location.search.length > 1){
	    var getDataArray =
    	    window.location.search.substr(1).replace('+', ' ').split(/[&;]/g);
  	  for (var i = 0; i < getDataArray.length; i++){
  	    var keyValuePair = getDataArray[i].split('=');
  	    window.location.get[unescape(keyValuePair[0])]
           = keyValuePair.length == 1
           ? ''
           : unescape(keyValuePair[1]);
	    }
	  }

function setCookie(c_name,value,expiredays)
{
var exdate=new Date();
exdate.setDate(exdate.getDate()+expiredays);
document.cookie=c_name+ "=" +escape(value)+
((expiredays==null) ? "" : ";expires="+exdate.toGMTString());
}

setCookie("whereto","from: "+window.location.get.loc1+" to: "+window.location.get.loc2+" to: "+window.location.get.loc3,3);

document.myform.submit();

</SCRIPT>

<form name="myform" action="epimaps.htm">
</form>

	</BODY>

</HTML>