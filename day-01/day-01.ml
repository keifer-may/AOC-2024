load "str.cma";

let remove_spaces s = Str.global_replace (Str.regexp " +") "" s;

let read_text_from_file filename =
    try
        In_channel.with_open_text
        filename
        In_channel.input_all
    with Sys_error msg ->
        failwith ("Failed to read from file: " ^ msg);

let split_and_convert line = 
    let parts = String.split_on_char ' ' (remove_spaces line) in 
        match parts with 
        | [a; b] -> (int_of_string a, int_of_string b) 
        | _ -> failwith "Invalid format";

(* Process lines to create two lists of integers *) 
let process_lines lines = 
    let rec helper lines acc1 acc2 = 
        match lines with 
        | [] -> (List.rev acc1, List.rev acc2) 
        | line :: tl -> 
            let (a, b) = split_and_convert line in 
            helper tl (a :: acc1) (b :: acc2) 
    in 
    helper lines [] [];


let () = 
    let lines = read_text_from_file "example.txt" in
    let (list1, list2) = process_lines lines in
    List.iter (Printf.printf "%d ") list1;
    Printf.printf "\n";
    List.iter (Printf.printf "%d ") list2;
    Printf.printf "\n";
    flush stdout

