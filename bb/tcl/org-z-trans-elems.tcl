proc main {} {
 set compname [hm_getstring "Component name" ""]
 *collectorcreateonly component $compname "" 9
 *clearmark elements 1
 *createmarkpanel elements 1 "Select elements"
 set thevector [*createvector 1 0.0 0.0 1.0]
 set thedistance [hm_getfloat "Distance" "Specify translation distance"]
 *translatemark elements 1 $thevector $thedistance
 *movemark elements 1 $compname
 *clearmark elements 1
}

main