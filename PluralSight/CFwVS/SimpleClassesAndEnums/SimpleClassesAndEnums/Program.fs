// Learn more about F# at http://fsharp.org
// See the 'F# Tutorial' project for more help.

type CarType =
    | Tricar
    | StandardFourWheeler
    | HeavyLoadCarrier
    | ReallyLargeTruck
    | CrazyHugeMythicalMonster
    | WeirdContraption

type Car(color:string, wheelCount:int) = 
    do
        if wheelCount = 2
        then failwith "That's a bike"
        elif wheelCount < 3
        then failwith "That's not enough wheels to be a 'car'"
    
    let carType =
        match wheelCount with
        | 3 -> Tricar
        | 4 -> StandardFourWheeler
        | 6 -> HeavyLoadCarrier
        | x when x % 2 = 1 -> WeirdContraption
        | _ -> CrazyHugeMythicalMonster

    member x.Move() = printfn "The %s car (%A) is moving" color carType

type RedSemi() =
    inherit Car("red", 18)

let greenCar = Car("green", 5)

greenCar.Move()

let carObj = greenCar :> obj