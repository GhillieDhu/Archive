for {set x 1357} {$x < 1474} {incr x} {
   *createmark solids 1  "all"
   *createplane 1 1.0000 0.0000 0.0000 $x -13.1100 97.7453 
   *body_splitmerge_with_plane solids 1 1 
}
