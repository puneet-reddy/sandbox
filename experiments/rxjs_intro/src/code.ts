import { Observable } from "rxjs/Observable";
import {merge} from 'rxjs/observable/merge';
import 'rxjs/add/operator/map';
// import 'rxjs/add/operator/share';
// import { fromEvent } from 'rxjs/Observable/fromEvent';
// import { Subject } from 'rxjs/Subject';
// import { BehaviorSubject } from 'rxjs/BehaviorSubject';
// import { ReplaySubject } from 'rxjs/ReplaySubject';
// import { AsyncSubject } from 'rxjs/AsyncSubject';


var observable1 = Observable.create((obs:any) => {
    obs.next('Observable1 says hi')
})

var observable2 = Observable.create((obs:any) => {
    obs.next('Observable2 says hi')
}).map((val:any) => val.toUpperCase())

// Operators are used to change the behavior of an observable.
// They don't mutate the input observable and instead return a new instance
var mergedObservable = merge(observable1, observable2)
var sub = mergedObservable.subscribe(
    (msg:any) => addItem(msg)
)

// A subject is both an observable and a subscriber at the same time.
// There are three types of subjects
// 1. A behavior subject - emits the last emitted value when subscribed to.
//      It needs a first value as an argument.
// 2. Replay subject - It has a buffer which lets you specify how many values
//      to dispatch to subscribers. Takes the buffer limit as an argument.
// 3. Async subject - It only emits the last value and only when the complete
//      method has been called on the subject.
// var subject = new AsyncSubject()

// subject.subscribe(
//     (data:any) => addItem('Observer1: '+data),
//     (err:any) => addItem(err),
//     () => addItem('Observer 1 completed')
// )

// var i = 1;
// var int = setInterval(() => subject.next(i++), 100);

// setTimeout(() => {
//     var subscriber1 = subject.subscribe(
//         (data:any) => addItem('Subscriber1: '+data)
//     )
//     subject.complete();
// }, 500);

// subject.next('This will not be sent to the second subscriber')
// subject.next('Nothing has been sent yet')
// subject.next("The first thing has been sent")

// var observer2 = subject.subscribe(
//     (data:any) => addItem('Observer2: '+data)
// )

// subject.next('The second thing has been sent')
// subject.next('The third thing has been sent')

// observer2.unsubscribe();

// subject.next("The fourth thing has been sent")

// // we're creating an observable from an event
// // There's a lot of creatable observables.
// var observable = fromEvent(document, 'mousemove');

// setTimeout(() => {
//     var subsription = observable.subscribe(
//         (x:any) => addItem(x)
//     )
// }, 2000);

// // This is a cold observable. i.e. the code in it executes when it is subscribed to
// // Adding a share operator makes the observable warm.
// var observable = Observable.create((observer: any) => {
//   try {
//     observer.next("Hello, world.");
//     observer.next("What is a world?");
//     setInterval(() => {
//       observer.next("I am the world!");
//     }, 2000);
//   } catch (err) {
//     observer.error(err);
//   }
// }).share();

// var observer = observable.subscribe(
//   (msg: any) => {
//     addItem(msg);
//   },
//   (error: any) => {
//     addItem(error);
//   },
//   () => {
//     addItem("completed");
//   }
// );

// var observer2 = observable.subscribe((x: any) => console.log(x));

// observer.add(observer2);

// setTimeout(() => {
//   observer.unsubscribe();
// }, 6001);

function addItem(val: any) {
  var node = document.createElement("li");
  var textNode = document.createTextNode(val);
  node.appendChild(textNode);
  document.getElementById("output").appendChild(node);
}
