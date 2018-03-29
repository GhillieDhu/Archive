<HTML>

	<HEAD>

		<TITLE>epimaps

		</TITLE>

		<link rel="shortcut icon" href="favicon.ico" type="image/vnd.microsoft.icon">		

		<SCRIPT type="text/javascript">

			function changeDiv(the_div,the_change)
			{
				var the_style = getStyleObject(the_div);
				if (the_style != false)
				{
					the_style.display = the_change;
				}
			}

			function getStyleObject(objectId)
			{
				if (document.getElementById && document.getElementById(objectId))
				{
					return document.getElementById(objectId).style;
				}
				else if (document.all && document.all(objectId))
				{
					return document.all(objectId).style;
				}
				else
				{
					return false;
				}
			}

			function showGroups()
			{
				var index = document.the_form.groups.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_'.concat(counter),'none')
				}
			}

			function showMembers1()
			{
				var index = document.the_form.Group_1_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_1_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_1_Stop_'.concat(counter),'none')
				}
			}

			function showMembers2()
			{
				var index = document.the_form.Group_2_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_2_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_2_Stop_'.concat(counter),'none')
				}
			}

			function showMembers3()
			{
				var index = document.the_form.Group_3_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_3_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_3_Stop_'.concat(counter),'none')
				}
			}

			function showMembers4()
			{
				var index = document.the_form.Group_4_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_4_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_4_Stop_'.concat(counter),'none')
				}
			}

			function showMembers5()
			{
				var index = document.the_form.Group_5_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_5_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_5_Stop_'.concat(counter),'none')
				}
			}

			function showMembers6()
			{
				var index = document.the_form.Group_6_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_6_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_6_Stop_'.concat(counter),'none')
				}
			}

			function showMembers7()
			{
				var index = document.the_form.Group_7_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_7_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_7_Stop_'.concat(counter),'none')
				}
			}

			function showMembers8()
			{
				var index = document.the_form.Group_8_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_8_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_8_Stop_'.concat(counter),'none')
				}
			}

			function showMembers9()
			{
				var index = document.the_form.Group_9_Members.options.selectedIndex+1;
				for (counter = 1; counter < index; counter++)
				{
					changeDiv('Group_9_Stop_'.concat(counter),'block')
				}
				for (counter = index; counter < 10; counter++)
				{
					changeDiv('Group_9_Stop_'.concat(counter),'none')
				}
			}
		</SCRIPT>

	</HEAD>

	<BODY bgColor=#7f7f7f>
		<H1>epimaps</H1>
		<FORM name="the_form" action="arraying.php" method="post">
			<INPUT type="radio" name="type" value="Round Trip" checked onclick="changeDiv('One_Way','none');">Round Trip<br>
			<INPUT type="radio" name="type" value="One Way" onclick="changeDiv('One_Way','block');">One Way<br>
			Origin: <input type="text" size="60" name="Origin"><br>
			<DIV id="One_Way" style="display:none">
				Destination: <input type="text" size="60" name="Destination"><br>
			</DIV>
			Intermediate Stops: <select name="groups" onchange="showGroups();">
				<option> -
				<option> 1
				<option> 2
				<option> 3
				<option> 4
				<option> 5
				<option> 6
				<option> 7
				<option> 8
				<option> 9
			</select><br>
			<DIV id="Group_1" style="margin-left:30px;display:none">
				<input type="text" name="Group_1_Label" value="Group 1">
				Members: <select name="Group_1_Members" onchange="showMembers1();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_1_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_1_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_1_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_2" style="margin-left:30px;display:none">
				<input type="text" name="Group_2_Label" value="Group 2">
				Members: <select name="Group_2_Members" onchange="showMembers2();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_2_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_2_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_2_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_3" style="margin-left:30px;display:none">
				<input type="text" name="Group_3_Label" value="Group 3">
				Members: <select name="Group_3_Members" onchange="showMembers3();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_3_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_3_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_3_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_4" style="margin-left:30px;display:none">
				<input type="text" name="Group_4_Label" value="Group 4">
				Members: <select name="Group_4_Members" onchange="showMembers4();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_4_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_4_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_4_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_5" style="margin-left:30px;display:none">
				<input type="text" name="Group_5_Label" value="Group 5">
				Members: <select name="Group_5_Members" onchange="showMembers5();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_5_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_5_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_5_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_6" style="margin-left:30px;display:none">
				<input type="text" name="Group_6_Label" value="Group 6">
				Members: <select name="Group_6_Members" onchange="showMembers6();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_6_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_6_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_6_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_7" style="margin-left:30px;display:none">
				<input type="text" name="Group_7_Label" value="Group 7">
				Members: <select name="Group_7_Members" onchange="showMembers7();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_7_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_7_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_7_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_8" style="margin-left:30px;display:none">
				<input type="text" name="Group_8_Label" value="Group 8">
				Members: <select name="Group_8_Members" onchange="showMembers8();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_8_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_8_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_8_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<DIV id="Group_9" style="margin-left:30px;display:none">
				<input type="text" name="Group_9_Label" value="Group 9">
				Members: <select name="Group_9_Members" onchange="showMembers9();">
					<option> -
					<option> 1
					<option> 2
					<option> 3
					<option> 4
					<option> 5
					<option> 6
					<option> 7
					<option> 8
					<option> 9
				</select><br>
				<DIV id="Group_9_Stop_1" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_1_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_2" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_2_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_3" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_3_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_4" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_4_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_5" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_5_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_6" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_6_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_7" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_7_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_8" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_8_Address">
				<br></DIV>
				<DIV id="Group_9_Stop_9" style="margin-left:60px;display:none">
					<input type="text" size="60" name="Group_9_Stop_9_Address">
				<br></DIV>
			<br></DIV>
			<input type="submit" value="Submit">
		</FORM>
	</BODY>

</HTML>