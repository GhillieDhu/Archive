proc main {} {
 *collectorcreateonly property kludgerot "" 0
 *createmark properties 1 kludgerot
 *dictionaryload properties 1 "C:/Altair/hw10.0/templates/feoutput/optistruct/optistruct" "PSHELL"
 set kurtgodel [hm_getmark properties 1]
 set kgthick [hm_getfloat "PSHELL Thickness"]
 *attributeupdatedouble properties $kurtgodel 95 1 1 0 $kgthick
}

main