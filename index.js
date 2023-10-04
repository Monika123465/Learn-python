//  check a no is prime or not
// let num=10
// count=0
// for(let i=1;i<=num;i++){
//     if(num%i==0){
//      count++
//     }
// }
// if(count==2){
//     console.log("the no is prime")
// }else{
//     console.log("the no is not prime")
// }

//  check how many prime no between a and b


// for (let counter = 0; counter <= 100; counter++) {

for(let  i=0;i<=100;i++){
    let flag=false
    for(let j=2;j<=i;j++){
        if(i%j===0 && j!==i){
            flag=true
        }
    }
    if(flag==false){
        console.log(i)
    }
}
