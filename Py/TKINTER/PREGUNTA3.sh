#! bin/bash
while [ 1 ]
do
    menor=0
    read -p "Ingrese un numero: " num1
	read -p "Ingrese numero 2: " num2
        if [ $num2 -ne $num1 ]
        then
        		read -p "Ingrese numero 3: " num3
                if [ $num3 -ne $num1 -a $num3 -ne $num2 ]
                then
				read -p "Ingrese numero 4: " num4
                	if [ $num4 -ne  $num3 -a $num4 -ne $num2 -a $num4 -ne $num1 ]
                	then
					read -p "Ingrese numero 5: " num5
                		if [ $num5 -ne $num4 -a $num5 -ne $num3 -a $num5 -ne $num2 -a $num5 -ne $num1 ]
		                then
						read -p "Ingrese numero 6: " num6
			                if [ $num6 -ne $num5 -a $num6 -ne $num4 -a $num6 -ne $num3 -a $num6 -ne $num2 -a $num6 -ne $num1 ]
			                then
							read -p "Ingrese numero 7: " num7
                				if [ $num7 -ne $num6 -a $num7 -ne $num5 -a $num7 -ne $num4 -a $num7 -ne $num3 -a $num7 -ne $num2 -a $num7 -ne $num1 ]
				                then
								read -p "Ingrese numero 8: " num8
					                if [ $num8 -ne $num7 -a $num8 -ne $num6 -a $num8 -ne $num5 -a $num8 -ne $num4 -a $num8 -ne $num3 -a $num8 -ne $num2 -a $num8 -ne $num1 ]
					                then
									for (( i=1 ; $i<8 ; i=$i+1 ))
									do
                                                			if [ $num2 -lt $num1 ]
	                                                		then
        	                                                	menor=$num2
                	                                        	num2=$num1
                        	                                	num1=$menor
                                	                		fi
                                        	        		if [ $num3 -lt $num2 ]
                                                			then
                                                        		menor=$num3
                                                        		num3=$num2
                                                        		num2=$menor
	                                                		fi
        	                                        		if [ $num4 -lt $num3 ]
                	                                		then 
                        	                                	menor=$num4 
                                	                        	num4=$num3
                                        	                	num3=$menor
                                                			fi
									if [ $num5 -lt $num4 ]
                                    then 
                                        menor=$num5 
	                                    num5=$num4
        	                            num4=$menor
                	            	fi
									if [ $num6 -lt $num5 ]
                                	then 
                                        menor=$num6 
                                        num6=$num5
                                        num5=$menor
                                    fi
									if [ $num7 -lt $num6 ]
	                                then 
        	                        	menor=$num7 
                	                	num7=$num6
                        	        	num6=$menor
                                	fi
									if [ $num8 -lt $num7 ]
                                    then 
                                        menor=$num8 
                                        num8=$num7
                                        num7=$menor
	                                                                fi
									done
								echo ">>Orden creciente:  $num1 - $num2 - $num3 - $num4 - $num5 - $num6 - $num7 - $num8"
                                    else
                                        echo ">>>Debe introducir un numero diferente"
                                    fi
                            	else
                                    echo ">>>Debe introducir un numero diferente"
		                        fi
                        	else
                                echo ">>>Debe introducir un numero diferente"
							fi
						else
							echo ">>>Debe introducir un numero diferente"
						fi
					else 
						echo ">>>Debe introducir un numero diferente"
					fi
				else
					echo ">>>Debe introducir un numero diferente"
				fi
			else
				echo ">>>Debe introducir un numero diferente"
			fi
done

