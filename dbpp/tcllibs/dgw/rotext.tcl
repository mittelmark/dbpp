#!/usr/bin/env tclsh
package require Tk
lappend auto_path [file join [file dirname [info script]] ..]
package require snit

namespace eval dgw { }

::snit::widgetadaptor ::dgw::rotext {

    constructor {args} {
        # Turn off the insert cursor
        #installhull using text $self -insertwidth 0 
        # DDG the $self gaves an error at least with 0.97 onwards
        installhull using text -insertwidth 0

        # Apply an options passed at creation time.
        $self configurelist $args
    }

    # Disable the insert and delete methods, to make this readonly.
    method insert {args} {}
    method delete {args} {}

    # Enable ins and del as synonyms, so the program can insert and
    # delete.
    delegate method ins to hull as insert
    delegate method del to hull as delete
    
    # Pass all other methods and options to the real text widget, so
    # that the remaining behavior is as expected.
    delegate method * to hull
    delegate option * to hull
}

package provide dgw::rotext 0.1

if {$argv0 eq [info script]} {
    # testing
    set rotext [dgw::rotext .rotext -wrap word]
    for {set i 0} {$i < 100} {incr i 1} {
        $rotext ins end [format "line: %02i Hello World!\n" $i]
    }
    pack $rotext -side top -fill both -expand true
}    
