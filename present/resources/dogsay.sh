#!/bin/bash

# A tiny script that has a dog say
# what needs to be said!

R="\033[1;31m"
G="\033[1;32m"
LG="\033[0;37m"
W="\033[1;37m"
Y="\033[0;33m"
D="\033[00m"

usage="USAGE:
# display the specified text
dogsay.sh talk \"\$(ls -ltr)\"
# display the specified text
# after wrapping it
dogsay.sh wrap \"\$(ls)\"
# display an animated dog
# with the specified message
dogsay.sh animate \"Loading...\"
# Wait on a PID
sleep 1 &
DOGSAY_WAIT_PID=$! ./dogsay.sh animate 'waiting...'
./dogsay.sh talk 'done!'
"

dog_barker="
${Y}          ${W}*${D}${Y}    ____${D}
${Y}             /  | ${W}o${Y}  \_ .${D}
${Y}   ${W}*${D}${Y}         \  |   '. /${D}
${Y}           /        |${D}
${Y}       ${W}*${D}${Y}  '         |  ${W}*${D}${Y}${D}
${Y}      ,  /     \ || |${D}
${Y}     // '   \  | || |${D}
${Y}    ||. '   /  | || |${D}
${Y}     \ \'.    ] 'mm'mm${D}
"

animated_dog=(
"
${Y}      ${LG}+${D}${Y}        ____   ${LG}+${D}${Y}${D}
${Y}          ${W}*${D}${Y}  /  | ${W}o${Y}  \_ .${D}
${Y}             \  |   '. /${D}
${Y}   ${W}*${D}${Y}       /        |${D}
${Y}          '         |${D}
${Y}      ,${W}*${D}${Y} /     \ || |  ${W}*${D}${Y}${D}
${Y}     // '   \  | || |  ${D}
${Y}    ||. '   /  | || |${D}
${Y}     \ \\'.    ] 'mm'mm${D}
"
"
${Y}   ${LG}+${D}${Y}           ____${D}
${Y}      ${LG}+${D}${Y}      /  | ${W}o${Y}  \_ .${D}
${Y}          ${W}*${D}${Y}  \  |   '. /${D}
${Y}           /        |${D}
${Y}   ${W}*${D}${Y}      '         |${D}
${Y}   '     /     \ || |${D}
${Y}   |\  ${W}*${D}${Y}'   \  | || |  ${W}*${D}${Y}${D}
${Y}     \.\'   /  | || |${D}
${Y}     ' \\'.    ] 'mm'mm${D}
"
"
${Y}               ____${D}
${Y}             /  | ${W}o${Y}  \_ .${D}
${Y}   ${LG}+${D}${Y}         \  |   '. /${D}
${Y}      ${LG}+${D}${Y}   ${W}*${D}${Y}/        | ${LG}+${D}${Y}${D}
${Y}          '         |${D}
${Y}      ,  /     \ || |${D}
${Y}    ${W}*${D}${Y}// '   \  | || |${D}
${Y}    ||. '   /  | || |  ${W}*${D}${Y}${D}
${Y}     \ \\'.    ] 'mm'mm${D}
"
"
${Y}               ____${D}
${Y}             /  | ${W}o${Y}  \_ .${D}
${Y}             \  |   '. /${D}
${Y}  ${LG}+${D}${Y}        /        |${D}
${Y}          '         | ${LG}+${D}${Y}${D}
${Y}   '  ${LG}+${D}${Y}  /     \ || |${D}
${Y}   |\   '   \  | || |${D}
${Y}     \.\'   /  | || |${D}
${Y}    ${W}*${D}${Y}' \\'.    ] 'mm'mm${W}*${D}${Y}${D}
"
"
${Y}      ${W}*${D}${Y}        ____${D}
${Y}             /  | ${W}o${Y}  \_ .${D}
${Y}             \  |   '. /${D}
${Y}           /        |${D}
${Y}  ${LG}+${D}${Y}       '         |${D}
${Y}      ,  /     \ || | ${LG}+${D}${Y}${D}
${Y}     // '   \  | || | ${D}
${Y}    ||. '   /  | || |${D}
${Y}     \ \\'.    ] 'mm'mm${D}
"
"
${Y}               ____${D}
${Y}      ${W}*${D}${Y}      /  | -  \_${W}*${D}${Y}.${D}
${Y}             \  |   '. /${D}
${Y}           /        |${D}
${Y}          '         |${D}
${Y}  ${LG}+${D}${Y}'     /     \ || |${D}
${Y}   |\   '   \  | || | ${LG}+${D}${Y}${D}
${Y}     \.\'   /  | || |${D}
${Y}     ' \\'.    ] 'mm'mm${D}
"
"
${Y}   ${W}*${D}${Y}          ${W}*${D}${Y}____${D}
${Y}             /  | ${W}o${Y}  \_ .${D}
${Y}      ${W}*${D}${Y}      \  |   '. /${D}
${Y}           /        |${D}
${Y}          '         |${D}
${Y}      ,  /     \ || |${D}
${Y}     // '   \  | || |${D}
${Y}  ${LG}+${D}${Y} ||. '   /  | || | ${LG}+${D}${Y}${D}
${Y}     \ \\'.    ] 'mm'mm${D}
"
"
${Y}               ____${D}
${Y}   ${W}*${D}${Y}         /  | ${W}o${Y}  \_ .${D}
${Y}             \  |   '. /${D}
${Y}      ${W}*${D}${Y}    /        |  ${W}*${D}${Y}${D}
${Y}          '         |${D}
${Y}   '     /     \ || |${D}
${Y}   |\   '   \  | || |${D}
${Y}     \.\'   /  | || |${D}
${Y}  ${LG}+${D}${Y}  ' \\'.    ] 'mm'mm${D}
"
)

# Erases the amount of lines specified.
delete_lines() {
  UP='\033[1A'
  for i in $(seq "$1"); do
    printf "$UP"
    printf "\033[2K"
  done
}

init_vars() {
    : "${dogsay_width:=50}"
    FOO="${VARIABLE:-default}"
    top_edge=$(printf %$(( dogsay_width + 2 ))s '' | tr ' ' -)
    bottom_edge0="--- "$(printf %$(( dogsay_width - 2 ))s '' | tr ' ' -)
    bottom_edge1="   V "
}

speechbubble_raw() {
    lines="$@"
    dogsay_width=$(echo "$lines" | col -b | awk '{print length}' |sort -nr|head -1)
    init_vars
    from_left="              "
    printf "${from_left} ${top_edge}\n"
    while read line; do
        printf "${from_left}| %-${dogsay_width}s |\n" "${line}";
    done < <(echo "$lines")
    printf "${from_left} ${bottom_edge0}\n"
    printf "${from_left} ${bottom_edge1}\n"

    LINE_LENGTHS=$(( $(echo "$lines" | wc -l) + 3 ))
}

speechbubble_wrapped() {
    init_vars
    lines=$(echo $@ | fmt -w $dogsay_width)
    speechbubble_raw "$lines"
}

animate() {
  while kill -0 $DOGSAY_WAIT_PID 2>/dev/null || [ -z "$DOGSAY_WAIT_PID" ]; do
    for i in "${animated_dog[@]}"
    do
      len=$(echo "$i" | wc -l)
      echo -e "$i"
      sleep .4
      delete_lines $len
    done
  done
  delete_lines $LINE_LENGTHS
}

case $1 in
    talk)
        shift
        speechbubble_raw "$@"
        printf "${dog_barker}\n"
        exit
        ;;
    wrap)
        shift
        speechbubble_wrapped "$@"
        printf "${dog_barker}\n"
        exit
        ;;
    animate)
        shift
        speechbubble_raw "$@"
        animate "$@"
        exit
        ;;
    animate_wrap)
        shift
        speechbubble_wrapped "$@"
        animate "$@"
        exit
        ;;
    *)
        speechbubble_raw "${usage}"
        echo "${dog_barker}"
        exit 1
        ;;
esac
