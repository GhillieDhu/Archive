###########################################################################################################################
#This macro is used to organize existing mesh into new components with the proeprties of the original mesh. 
#The properties thus created can later be used to define desvar for gage optimization
#
#
#
#
# Macro updated to work with HM9.0 by Vaibhav Ekote vaibhav@altair.com on 26th Sep 2008
#
#
###########################################################################################################################
set install_home [ hm_info -appinfo ALTAIR_HOME ]
proc CheckTemplate { args } {

    ##Determine which template is loaded to decide which solver database to use
     set template [hm_info templatefilename]

     if {([string first "nastran" [string tolower $template]] == -1) && ([string first "optistruct" [string tolower $template]] == -1) } {

     tk_messageBox -icon error -title "Conversion" -message "Utility only supported in OptiStruct or Nastran User Profile!";
     return -code 0 -errorinfo "Macro aborted" -errorcode 0
     } else { main } 
}


hm_markclear elems 1
hm_blockmessages 1
 
*entityhighlighting 1
hm_blockerrormessages 1
hm_commandfilestate 0

proc main {} {

for {set z 0} {$z < 50} {incr z} {  
#*createmarkpanel elems 1 "select elements to organize into new components&properties"

set elems_list [hm_getmark elems [ *createmarkpanel elems 1 "select elements to organize into new components&properties" ] ]

if { [ Null elems_list ] } {

       tk_messageBox -icon error -title "macro error" -message "No elements selected. Exiting."
       
        return
       
        }
        


*entityhighlighting 0 

set numElems [ llength $elems_list ]
set prop_id_list []

set all_PROPS [ hm_getmark PROPS [ *createmark PROPS 1 all ]]


foreach e $elems_list {

		set propID [hm_getentityvalue elems $e "propertyid" 0]

		set propName [hm_getcollectorname property $propID ]

if { [ lsearch $prop_id_list "$propID" ] == -1 } {

lappend prop_id_list $propID
  }


 


}

set numProps [ llength $prop_id_list ]
set prop_new_list []
set comp_new_list []
set maxId [hm_entitymaxid comps]
set compColor [hm_getentityvalue COMPONENTS $maxId "color" 0]

if {$compColor >=  64} {
		        set hmcolor 9} else {
		    		     	  
					set hmcolor [ expr {$compColor+1}]
   }					
#set hmcolor [ expr {$compColor+8}]
set count [ expr {$maxId+1}]
set auto auto
  #puts $propID
  #puts $prop_id_list
  #puts $prop_name_list
 
foreach p $prop_id_list {
                    set matId [hm_getentityvalue property $p "materialid" 0]
                    set matName [hm_getcollectorname material $matId]
                    set propName [hm_getcollectorname property $p ]
                   
                    #if { [ lsearch $all_PROPS "$propName\_$auto\_$count" ] == -1 } {
                    *collectorcreatesameas properties "$propName\_$auto\_$count" "$propName" "$matName" $hmcolor
                    set new_prop [hm_getmark props [*createmark props 2 -1]]
                    lappend prop_new_list "$propName\_$auto\_$count"
                    hm_markclear props 2
                    set compName [*collectorcreateonly components "$propName\_$auto\_$count" ""  $hmcolor]
                    lappend comp_new_list "$propName\_$auto\_$count"
		    *createmark components 1  "$propName\_$auto\_$count"
		    *propertyupdate components 1 "$propName\_$auto\_$count" 
                    
                     incr count
                     #}
		    		     	 if {$hmcolor > 64} {
		    				 set hmcolor 9
		    		     	 } else {
		    				 set hmcolor [ expr {$hmcolor+7}]
		    		     	 }
	
		 #puts $prop_new_list 
		 
} 


                #puts $comp_new_list
               
               
 foreach e $elems_list {

 		set propID [hm_getentityvalue elems $e "propertyid" 0]

 		set old_prop_Name [hm_getcollectorname property $propID ]
 		
 		set matching_prop_index [lsearch $prop_new_list *$old_prop_Name* ]
		
		set matching_comp_name [lindex  $comp_new_list  $matching_prop_index]
 		
                #puts  $matching_prop_index
                #$puts  $matching_comp_name
                 
                *createmark elements 1 $e
                *movemark elems 1  "$matching_comp_name"
 

                         }
*entityhighlighting 1                         
}
}
CheckTemplate

*entityhighlighting 1
hm_blockerrormessages 0
#hm_usermessage "$count Properties and Components Created."
hm_blockmessages 0
hm_commandfilestate 1

 
