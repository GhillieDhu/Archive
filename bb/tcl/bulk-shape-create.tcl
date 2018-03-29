proc gethandles {} {
    *clearmark handles 1
    *createmarkpanel handles 1 "Select Handles"
    hm_getmark handles 1
}

proc getsystem {} {
    *clearmark systems 1
    *createmarkpanel systems 1 "Select System"
    hm_getmark systems 1
}

proc main {} {
    set thehandles [gethandles]
    set shapenameprefix [hm_getstring "Shape name prefix: "]
    set thesystem [getsystem]
    set x [hm_getfloat "x: "]
    set y [hm_getfloat "y: "]
    set z [hm_getfloat "z: "]
    set firstshapenumber [hm_entitymaxid shapes]
    foreach h $thehandles {
        set nextshapenumber [expr {[hm_entitymaxid shapes]+1}]
        *clearmark handles 2
        *createmark handles 2 $h
        *morphhandlepertxyz handles 2 $x $y $z $thesystem 1 1
        *morphshapecreatecolor $shapenameprefix$nextshapenumber 0 15
        *morphdoshape 1
    }
    set lb [hm_getfloat "Lower bound: "]
    set ub [hm_getfloat "Upper bound: "]
    for {set sh $firstshapenumber} {$sh < [hm_entitymaxid shapes]} {incr sh} {
        set thesh [expr {$sh + 1}]
        *shpdesvarcreate $shapenameprefix$thesh $ub [expr {($ub + $lb) / 2}] $lb -1 $thesh
    }
}

main
