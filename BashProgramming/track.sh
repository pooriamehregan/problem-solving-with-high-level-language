#!/bin/bash
user="pooriamehregan"
LOGFILE=/Users/${user}/.local/share/LOGFILE
declare -i count=0

# checks if LOGFILE path exist, if not, it creates it.
function create_path {
    if [ $count == 0 ]; then
        if [ ! -d "/Users/${user}/.local" ]; then
          mkdir "/Users/${user}/.local"
        fi
        if [ ! -d "/Users/${user}/.local/share" ]; then
          mkdir "/Users/${user}/.local/share"
        fi
        if [ ! -f "/Users/${user}/.local/share/LOGFILE" ]; then
          touch "/Users/${user}/.local/share/LOGFILE"
        fi
        count=1
    fi
}


# works as the main function
function track() {
    create_path
    last_word=$(tail -n1 $LOGFILE | cut -d' ' -f1)
    # number of command line args is at least 2 (grater than 0 because shell extracts script name from counter).
    if [ $# -gt 0 ]; then
        # if LOGFILE is not empty and first word of the last line != END, set bool to true, and false otherwise.
        if [ -s $LOGFILE ] && [ "$last_word" != "END" ] ; then
            bool=true
        else
            bool=false
        fi
        
        if [ "$1" == "start" ]; then
            if [ "$bool" == true ]; then
                printf "Another task is running. \
                    \nUse command <track stop> to stop the running task.\n"
                exit 1
            elif [ $# -ne 2 ]; then
                echo "LABEL argument is missing!"
                exit 1
            else # every is okey, start this task
                date=$(date)
                printf "\nSTART <${date}>\nLABEL <${2}>\n" >> $LOGFILE
            fi
        elif [ "$1" == "stop" ]; then
            if [ "$bool" = true ]; then
                printf "END   <$(date)>\n" >> $LOGFILE
            else
                echo "No task is running!"
            fi
        elif [ "$1" == "status" ]; then
            if [ "$bool" == true ]; then
                tail -n2 $LOGFILE
            else
                echo "No active task!"
            fi
        fi
    fi
}


# this is a helper function to log. Converts seconds to formated time HH:MM:SS.
function convert_secs(){
    ((h=${1}/3600))
    ((m=(${1}%3600)/60))
    ((s=${1}%60))
    printf "%02d:%02d:%02d\n" $h $m $s
}

# beware this tracker does not track days,months and years, just tasks whith durations less than 24 hours, becasue excercise didn't require it given the example that was there.
function log {
    starts=$(grep "START" $LOGFILE | cut -d" " -f6)
    ends=$(grep "END" $LOGFILE | cut -d" " -f8)
    labels=$(grep "LABEL" $LOGFILE | cut -d" " -f2,3)
    
    start_array=($(echo $starts | tr " " "\n"))
    end_array=($(echo $ends | tr " " "\n"))
    IFS=$'\n' read -rd '' -a label_array <<<"$labels"
    #label_array=($(echo $labels | tr '' "\n" ))
    
    if [ ${#start_array[@]} -ne ${#end_array[@]} ]; then

        end_array+=($(date +"%H:%M:%S"))

    fi
    
    declare -i counter=0
    declare -i start=0; declare -i end=0; declare -i dif=0
    #Print the split string
    for i in ${start_array[@]}
    do
        start=$(echo $i | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
        end=$(echo ${end_array[${counter}]} | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }')
        dif=$((end - start))

        printf "${label_array[$counter]}    $(convert_secs $dif)\n"
        ((counter++))
    done
}






    
