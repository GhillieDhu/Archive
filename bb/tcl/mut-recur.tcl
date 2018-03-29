proc a {x text} {
 if {$x} {
  puts "grr"
 } else {
  puts "ugh"
  b $text
 }
}

proc b arg {
 a 1 arg
}

proc main {} {
 a 0 "woo-hoo"
}

main