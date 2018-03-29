open System

type FizzBuzzEvent = {label:int; time: DateTime}

let areSimultaneous (earlierEvent, laterEvent) =
    let {label = _; time = t1} = earlierEvent
    let {label = _; time = t2} = laterEvent
    t2.Subtract(t1).Milliseconds < 50

let createTimerAndObservable timerInterval =
    // setup a timer
    let timer = new System.Timers.Timer(float timerInterval)
    timer.AutoReset <- true

    // events are automatically IObservable
    let observable = timer.Elapsed

    // return an async task
    let task = async {
        timer.Start()
        do! Async.Sleep 5000
        timer.Stop()
        }

    // return a async task and the observable
    (task, observable)

let timer3, timerEventStream3 = createTimerAndObservable 300
let timer5, timerEventStream5 = createTimerAndObservable 500

// convert the time events into FizzBuzz events with the appropriate id
let eventStream3 =
    timerEventStream3
    |> Observable.map (fun _ -> {label = 3; time = DateTime.Now})

let eventStream5  =
    timerEventStream5
    |> Observable.map (fun _ -> {label = 5; time = DateTime.Now})

// combine the two streams
let combinedStream =
    Observable.merge eventStream3 eventStream5

// make pairs of events
let pairwiseStream =
    combinedStream
    |> Observable.pairwise

// split the stream based on whether the pairs are simultaneous
let simultaneousStream, nonSimultaneousStream =
    pairwiseStream
    |> Observable.partition areSimultaneous

// split the non-simultaneous stream based on the id
let fizzStream, buzzStream =
    nonSimultaneousStream
    |> Observable.map (fun (ev1, _) -> ev1) // convert pair of events to the first event
    |> Observable.partition (fun {label = id} -> id = 3) // split on whether the event id is three

//print events from the combinedStream
combinedStream 
|> Observable.subscribe (fun {label = id; time = t} -> 
                              printf "[%i] %i.%03i " id t.Second t.Millisecond)
|> ignore
 
//print events from the simultaneous stream
simultaneousStream 
|> Observable.subscribe (fun _ -> printfn "FizzBuzz")
|> ignore

//print events from the nonSimultaneous streams
fizzStream 
|> Observable.subscribe (fun _ -> printfn "Fizz")
|> ignore

buzzStream 
|> Observable.subscribe (fun _ -> printfn "Buzz")
|> ignore

// run the two timers at the same time
[timer3;timer5]
|> Async.Parallel
|> Async.RunSynchronously
|> ignore

