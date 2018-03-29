// Learn more about F# at http://fsharp.org
// See the 'F# Tutorial' project for more help.
open SturmDemo

let intVal = 100

let strVal = "hi there"

let boolVal = true

let floatVal = 12.3

let deciVal = 47.99m

let mult x y =
    (float x) * (float y)

printfn "%A" (mult 3.2 4)

let coeff3 = mult 3.0

printfn "%A" (coeff3 5)

let result = Calculator.add (Calculator.square 12) 7

printfn "%A" result







[<EntryPoint>]
let main argv = 
//    printfn "%A" argv
    0 // return an integer exit code