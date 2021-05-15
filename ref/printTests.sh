#!/bin/bash
read -p 'Please enter Grammar Book Level: ' grammar_level
read -p 'Please enter start page: ' start_page
read -p 'Please enter end page: ' end_page

#start_page=1
#end_page=20

for ((i=end_page; i>=start_page; i--))
do
    lesson_num=$(printf "%02d" $i)
    if (( $grammar_level <= 3 ))
    then
        dir="My First Grammar $grammar_level"
    else
        next_grammar_level=$(($grammar_level-3))
        dir="My Next Grammar $next_grammar_level"
    fi
    lp -o fit-to-page -o page-ranges=1 -o outputorder=reverse -n 1 "$dir/Lesson $lesson_num Test.pdf";
    echo $(printf "Printing test page %s - #%s" "$dir" $lesson_num)
done

