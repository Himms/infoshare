<?php ob_start();

                             ini_set("display_errors", 1);
                             $output = shell_exec("Python3 /Users/himms/Laravel/infoshare/resources/views/script.py 2>&1" );
                              print($output);
                              
                           //  exec('python3 --version 2>&1', $output);
                            // var_dump ($output);
                             //print($output);
                             //https://colab.research.google.com/drive/1SccxAygr16BmnRPt8DuUm8OY7hPm_qdw?usp=sharing
                            //Execute the command
                             //$output = [];
                             //$returnValue = null;
                            // exec($command, $output, $returnValue);
                           //source  /Users/himms/Laravel/infoshare/resources/views/venv/bin/Activate
                             // Check if the command executed successfully
                            // if ($returnValue === 0) {
                                 // Process the output
                              //   foreach ($output as $line) {
                                 
                               //      print('');
                              //   }
                             //} else {
                                 // Handle the case where the command failed to execute
                            // }
                            if($output>0){
                            exit("The required file does not exist.");
                         }
    ob_end_flush();                                     
                            
                             
