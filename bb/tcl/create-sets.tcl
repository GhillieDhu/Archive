proc more_pred {} {
 set old [hm_marklength elements 1]
 set new [hm_marklength elements 2]
 return [expr $new - $old]
}

proc get_one_set {} {
 *clearmark sets 1
 *createmarkpanel sets 1 "Select Set"
 if {[hm_marklength sets 1] > 1} {
  get_one_set
 } else {if {[hm_marklength sets 1] == 0} {
  *clearmark elements 1
  *createmarkpanel elements 1 "Select Elements"
  *entitysetcreate [hm_getstring "Set name:" "Specify set name"] elements 1
  *clearmark elements 1
 }}
 *clearmark elements 2
 hm_getentityvalue sets [hm_getmark sets 1] "name" 1
}

proc build_element_marks {} {
 *clearmark elements 1
 *clearmark elements 2
 *createmark elements 1 "by set" [hm_getmark sets 1]
 *createmark elements 2 "by set" [hm_getmark sets 1]
 hm_appendmark elements 2 "advanced" "by adjacent"
}

proc main {} {
 set set_name [get_one_set]
 puts $set_name
 build_element_marks
 while {[more_pred] > 0} {
  set next_set_id [expr 1+[hm_entitymaxid sets]]
  *entitysetcreate $set_name$next_set_id elements 2
  *clearmark sets 1
  *createmark sets 1 $set_name$next_set_id
  build_element_marks
 }
 *clearmark sets 1
}

main