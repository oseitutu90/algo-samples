// minimumBribes takes an array of integers and returns t
//he minimum number of bribes that took place to get the queue into its current state.

function minimumBribes(q) {
    let bribes = 0;
    for (let i = 0; i < q.length; i++) {
        if (q[i] - (i + 1) > 2) {
            console.log("Too chaotic"); 
            return;
        }
        for (let j = q[i] - 2; j < i; j++) { // j = q[i] - 2 because the person can only bribe 2 people
            if (q[j] > q[i]) bribes++;
        }
    }
    console.log(bribes);
}

console.log(minimumBribes([2, 1, 5, 3, 4])); // 3