proc get_lines {input_file} {
    set raw [open $input_file r]
    set mod [read $raw]
    close $raw
    set lines [split $mod \n]
    return $lines
}

proc merge {cells divisor} {
    set strung [lindex $cells 0]
    lappend strung " "
    for {set i 1} {$i < [llength $cells]} {incr i} {
        lappend strung [format "% 11.3E" [expr [lindex $cells $i] / $divisor]]
    }
    return [format " %s" [join $strung]]
}

proc main {input_file output_file} {
    set lines [get_lines $input_file]
    set replaced {}
    set aggregate {}
    set count 0
    for {set i 0} {$i < [llength $lines]} {incr i} {
        if {[llength [lindex $lines $i]] == 9} {
            incr count
            if {[llength $aggregate] == 0} {
                lappend aggregate " AVERAGE  "
                for {set j 1} {$j < [llength [lindex $lines $i]]} {incr j} {
                    lappend aggregate [expr double([lindex [lindex $lines $i] $j])]
                }
            } else {
                for {set j 1} {$j < [llength [lindex $lines $i]]} {incr j} {
                    lset aggregate $j [expr double([lindex [lindex $lines $i] $j]) + [lindex $aggregate $j]]
                }
            }
        } else {
            if {[llength $aggregate] > 0} {
                lappend replaced [merge $aggregate $count]
            }
            lappend replaced [lindex $lines $i]
            set aggregate {}
            set count 0            
        }
    }
    if {[llength $aggregate] > 0} {
        lappend replaced [merge $aggregate $count]
    }
    set dump [open $output_file w]
    puts $dump [join $replaced \n]
    close $dump
}

#main [lindex $argv 0] [lindex $argv 1]
