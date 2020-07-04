function getSum(num1: number, num2: number): number {
    return num1 + num2;
}

// console.log(getSum(1, 2));

function getName(first?: string, last?: string): string {
    if (first == undefined) {
        first = 'John'
    }
    if (last == undefined) {
        return first;
    }
    return first + ' ' + last;
}

console.log(getName('John', 'Doe'));
console.log(getName());