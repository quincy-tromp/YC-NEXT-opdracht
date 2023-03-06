#!/bin/zsh

read -p "Which would you choose: cake, cookie, apple? " answer

if [ $answer == "cake" ]; 
then 
  echo "Good choice. Life is short, eat the cake."
elif [ $answer == "cookie" ];
then 
  echo "Nice one. Cookies make the world a better place."
elif [ $answer == "apple" ];
then 
  echo "Great choice. An apple a day keeps the doctor away."
else 
  echo "$answer is not a valid option."
fi
