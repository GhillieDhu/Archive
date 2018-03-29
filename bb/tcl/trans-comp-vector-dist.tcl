proc main {} {
 set thecomponent [getcomponent]
 set thevector [getvector]
 set thedistance [getdistance]
 transcompvectdist $thecomponent $thevector $thedistance
}

proc getcomponent {} {
 *clearmark components 1
 *createmarkpanel components 1 "Select Component"
 hm_getmark components 1
}

proc getvector {} {
 *clearmark vectors 1
 *createmarkpanel vectors 1 "Select Vector"
 hm_getmark vectors 1
}

proc getdistance {} {
 hm_getfloat "Distance" "Specify translation distance"
}

proc transcompvectdist {acomp avect adist} {
 set xraw [hm_getentityvalue vectors $avect.id "xcomp" 0 -byid]
 set yraw [hm_getentityvalue vectors $avect.id "ycomp" 0 -byid]
 set zraw [hm_getentityvalue vectors $avect.id "zcomp" 0 -byid]
 set vectmag [hm_getentityvalue vectors $avect.id "magnitude" 0 -byid]
 *createvector 2 $xraw $yraw $zraw
 *translatemark components 1 2 $adist
 *clearmark components 1
 *clearmark vectors 1
}

main