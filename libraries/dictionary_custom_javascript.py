dictionary = {
    'type': 'javascript',
    'terms': [
     {
        'name': 'findIndex',
        'trigger': 'find index',
        'define': """The 'findIndex()' method is part of the Array object in JavaScript. It returns the index of the first element in the array that satisfies a provided testing function. If no elements satisfy the testing function, it returns -1. The function is not invoked for index properties that have been deleted or are uninitialized. This method does not mutate the array on which it is called, but the function provided will be called for every element in the array until it finds one where it returns a truthy value. If such an element is found, 'findIndex()' immediately returns the element's index. If the callback never returns a truthy value (or the array's length is 0), 'findIndex()' returns -1.

Syntax:
array.findIndex(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that tests each element of the array. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'findIndex()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'findIndex()' method returns the index of the first element in the array that satisfies the provided testing function; otherwise, it returns -1.

Examples:
1. Finding the index of the first element greater than 10:
let numbers = [5, 12, 8, 130, 44];
let isLargeNumber = (element) => element > 10;
let index = numbers.findIndex(isLargeNumber);
console.log(index); // Output: 1 (index of the element 12)

2. Finding the index of the first negative number:
let numbers = [-1, -2, 3, 4, 5];
let isNegative = (element) => element < 0;
let index = numbers.findIndex(isNegative);
console.log(index); // Output: 0 (index of the element -1)

3. Using 'thisArg' to set the context in the callback function:
let numbers = [1, 2, 3, 4, 5];
let targetValue = 3;
function isTarget(element) {
    return element === this.target;
}
let index = numbers.findIndex(isTarget, { target: targetValue });
console.log(index); // Output: 2 (index of the element 3)""",
        'example': """
            // Example 1:
            let numbers = [5, 12, 8, 130, 44];
            let isLargeNumber = (element) => element > 10;
            let index = numbers.findIndex(isLargeNumber);
            console.log(index); // Output: 1

            // Example 2:
            let numbers = [-1, -2, 3, 4, 5];
            let isNegative = (element) => element < 0;
            let index = numbers.findIndex(isNegative);
            console.log(index); // Output: 0

            // Example 3:
            let numbers = [1, 2, 3, 4, 5];
            let targetValue = 3;
            function isTarget(element) {
                return element === this.target;
            }
            let index = numbers.findIndex(isTarget, { target: targetValue });
            console.log(index); // Output: 2
        """
    },
    {
        'name': 'find',
        'define': """The 'find()' method returns the value of the first element in the provided array that satisfies the provided testing function. If no values satisfy the testing function, undefined is returned. The 'find' method executes the callback function once for each index of the array until it finds one where the callback returns a truthy value. If such an element is found, 'find()' immediately returns the value of that element. Otherwise, 'find()' returns undefined.

Syntax:
array.find(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that tests each element of the array. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'find()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'find()' method returns the value of the first element in the array that satisfies the provided testing function; otherwise, it returns undefined.

Examples:
1. Finding the first element greater than 10:
let numbers = [5, 12, 8, 130, 44];
let isLargeNumber = (element) => element > 10;
let found = numbers.find(isLargeNumber);
console.log(found); // Output: 12 (the first element greater than 10)

2. Finding the first negative number:
let numbers = [-1, -2, 3, 4, 5];
let isNegative = (element) => element < 0;
let found = numbers.find(isNegative);
console.log(found); // Output: -1 (the first negative number)

3. Using 'thisArg' to set the context in the callback function:
let fruits = ['apple', 'orange', 'banana'];
function findFruit(fruit) {
    return this.target === fruit;
}
let targetFruit = 'banana';
let found = fruits.find(findFruit, { target: targetFruit });
console.log(found); // Output: 'banana' (the target fruit)
""",
        'example': """
            // Example 1:
            let numbers = [5, 12, 8, 130, 44];
            let isLargeNumber = (element) => element > 10;
            let found = numbers.find(isLargeNumber);
            console.log(found); // Output: 12

            // Example 2:
            let numbers = [-1, -2, 3, 4, 5];
            let isNegative = (element) => element < 0;
            let found = numbers.find(isNegative);
            console.log(found); // Output: -1

            // Example 3:
            let fruits = ['apple', 'orange', 'banana'];
            function findFruit(fruit) {
                return this.target === fruit;
            }
            let targetFruit = 'banana';
            let found = fruits.find(findFruit, { target: targetFruit });
            console.log(found); // Output: 'banana'
        """
    },
    {
        'name': 'fill',
        'define': """The 'fill()' method changes all elements in an array to a static value, from a start index (default 0) to an end index (default array length). It mutates the original array and returns the modified array.

Syntax:
array.fill(value[, start[, end]])

Parameters:
- 'value' (required): The value to fill the array with.
- 'start' (optional): The index to start filling the array (default is 0).
- 'end' (optional): The index to stop filling the array (default is array.length).

Return Value:
The 'fill()' method returns the modified array.

Examples:
1. Filling an array with a specific value:
let array = [1, 2, 3, 4, 5];
array.fill(0);
console.log(array); // Output: [0, 0, 0, 0, 0]

2. Filling a portion of an array with a specific value:
let array = [1, 2, 3, 4, 5];
array.fill(0, 1, 4);
console.log(array); // Output: [1, 0, 0, 0, 5]

3. Filling an array with objects:
let array = new Array(3);
array.fill({ key: 'value' });
console.log(array); // Output: [{ key: 'value' }, { key: 'value' }, { key: 'value' }]
""",
        'example': """
            // Example 1:
            let array = [1, 2, 3, 4, 5];
            array.fill(0);
            console.log(array); // Output: [0, 0, 0, 0, 0]

            // Example 2:
            let array = [1, 2, 3, 4, 5];
            array.fill(0, 1, 4);
            console.log(array); // Output: [1, 0, 0, 0, 5]

            // Example 3:
            let array = new Array(3);
            array.fill({ key: 'value' });
            console.log(array); // Output: [{ key: 'value' }, { key: 'value' }, { key: 'value' }]
        """
    },
    {
        'name': 'from',
        'define': """The 'from()' method is a static method of the Array object that creates a new shallow-copied array from an array-like or iterable object. It allows converting objects that are not actual arrays (such as NodeList, arguments, or strings) into arrays.

Syntax:
Array.from(arrayLike[, mapFn[, thisArg]])

Parameters:
- 'arrayLike' (required): An array-like or iterable object to convert to an array.
- 'mapFn' (optional): A function to map each element of the array.
- 'thisArg' (optional): An object to use as 'this' when executing the map function.

Return Value:
The 'from()' method returns a new Array instance.

Examples:
1. Converting a string to an array:
let str = 'hello';
let array = Array.from(str);
console.log(array); // Output: ['h', 'e', 'l', 'l', 'o']

2. Converting a NodeList to an array:
let nodeList = document.querySelectorAll('p');
let array = Array.from(nodeList);
console.log(array); // Output: [p1, p2, p3, ...]

3. Using the map function to manipulate elements during conversion:
let numbers = [1, 2, 3, 4, 5];
let doubledArray = Array.from(numbers, (num) => num * 2);
console.log(doubledArray); // Output: [2, 4, 6, 8, 10]
""",
        'example': """
            // Example 1:
            let str = 'hello';
            let array = Array.from(str);
            console.log(array); // Output: ['h', 'e', 'l', 'l', 'o']

            // Example 2:
            let nodeList = document.querySelectorAll('p');
            let array = Array.from(nodeList);
            console.log(array); // Output: [p1, p2, p3, ...]

            // Example 3:
            let numbers = [1, 2, 3, 4, 5];
            let doubledArray = Array.from(numbers, (num) => num * 2);
            console.log(doubledArray); // Output: [2, 4, 6, 8, 10]
        """
    },
    {
        'name': 'forEach',
        'trigger': 'for each',
        'define': """The 'forEach()' method executes a provided function once for each array element. It is a higher-order function used for iterating over arrays.

Syntax:
array.forEach(callback(currentValue[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function to execute for each element in the array. It takes three arguments:
    - 'currentValue': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'forEach()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'forEach()' method does not return a value. It is executed for its side effects.

Examples:
1. Using 'forEach()' to log each element in the array:
let numbers = [1, 2, 3, 4, 5];
numbers.forEach((num) => {
    console.log(num);
});
// Output: 1
//         2
//         3
//         4
//         5

2. Using 'forEach()' with an object method:
let obj = {
    name: 'John',
    age: 30,
    country: 'USA',
};
Object.keys(obj).forEach((key) => {
    console.log(key + ': ' + obj[key]);
});
// Output: name: John
//         age: 30
//         country: USA

3. Using 'forEach()' with 'thisArg':
function logEvenNumbers(num) {
    if (num % 2 === 0) {
        console.log(num);
    }
}
let numbers = [1, 2, 3, 4, 5];
numbers.forEach(logEvenNumbers, { target: 2 });
// Output: 2
//         4
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            numbers.forEach((num) => {
                console.log(num);
            });
            // Output: 1
            //         2
            //         3
            //         4
            //         5

            // Example 2:
            let obj = {
                name: 'John',
                age: 30,
                country: 'USA',
            };
            Object.keys(obj).forEach((key) => {
                console.log(key + ': ' + obj[key]);
            });
            // Output: name: John
            //         age: 30
            //         country: USA

            // Example 3:
            function logEvenNumbers(num) {
                if (num % 2 === 0) {
                    console.log(num);
                }
            }
            let numbers = [1, 2, 3, 4, 5];
            numbers.forEach(logEvenNumbers, { target: 2 });
            // Output: 2
            //         4
        """
    },
    {
        'name': 'filter',
        'define': """The 'filter()' method creates a new array with all elements that pass the test implemented by the provided function. It is a higher-order function used for filtering elements in an array based on a condition.

Syntax:
array.filter(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that tests each element of the array. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'filter()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'filter()' method returns a new array containing all elements that pass the test implemented by the provided callback function.

Examples:
1. Filtering even numbers from an array:
let numbers = [1, 2, 3, 4, 5];
let evenNumbers = numbers.filter((num) => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]

2. Filtering objects based on a condition:
let products = [
    { id: 1, name: 'Laptop', price: 1000 },
    { id: 2, name: 'Phone', price: 500 },
    { id: 3, name: 'Tablet', price: 300 },
];
let affordableProducts = products.filter((product) => product.price < 800);
console.log(affordableProducts);
// Output: [
//     { id: 2, name: 'Phone', price: 500 },
//     { id: 3, name: 'Tablet', price: 300 },
// ]

3. Filtering elements using 'thisArg':
function isBelowThreshold(value) {
    return value < this.threshold;
}
let numbers = [1, 2, 3, 4, 5];
let filteredNumbers = numbers.filter(isBelowThreshold, { threshold: 4 });
console.log(filteredNumbers); // Output: [1, 2, 3]
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let evenNumbers = numbers.filter((num) => num % 2 === 0);
            console.log(evenNumbers); // Output: [2, 4]

            // Example 2:
            let products = [
                { id: 1, name: 'Laptop', price: 1000 },
                { id: 2, name: 'Phone', price: 500 },
                { id: 3, name: 'Tablet', price: 300 },
            ];
            let affordableProducts = products.filter((product) => product.price < 800);
            console.log(affordableProducts);
            // Output: [
            //     { id: 2, name: 'Phone', price: 500 },
            //     { id: 3, name: 'Tablet', price: 300 },
            // ]

            // Example 3:
            function isBelowThreshold(value) {
                return value < this.threshold;
            }
            let numbers = [1, 2, 3, 4, 5];
            let filteredNumbers = numbers.filter(isBelowThreshold, { threshold: 4 });
            console.log(filteredNumbers); // Output: [1, 2, 3]
        """
    },
    {
        'name': 'flat',
        'define': """The 'flat()' method creates a new array with all sub-array elements concatenated into it recursively up to the specified depth. It effectively flattens nested arrays.

Syntax:
array.flat([depth])

Parameters:
- 'depth' (optional): The depth level specifying how deep a nested array structure should be flattened. The default is 1.

Return Value:
The 'flat()' method returns a new array with the sub-array elements concatenated to the specified depth.

Examples:
1. Flattening a nested array:
let nestedArray = [1, [2, 3], [4, [5]]];
let flattenedArray = nestedArray.flat();
console.log(flattenedArray); // Output: [1, 2, 3, 4, [5]]

2. Flattening a nested array with depth specified:
let deeplyNestedArray = [1, [2, [3, [4]]]];
let flattenedArray = deeplyNestedArray.flat(Infinity);
console.log(flattenedArray); // Output: [1, 2, 3, 4]
""",
        'example': """
            // Example 1:
            let nestedArray = [1, [2, 3], [4, [5]]];
            let flattenedArray = nestedArray.flat();
            console.log(flattenedArray); // Output: [1, 2, 3, 4, [5]]

            // Example 2:
            let deeplyNestedArray = [1, [2, [3, [4]]]];
            let flattenedArray = deeplyNestedArray.flat(Infinity);
            console.log(flattenedArray); // Output: [1, 2, 3, 4]
        """
    },
    {
        'name': 'flatMap',
        'trigger': 'flat map',
        'define': """The 'flatMap()' method combines 'map()' and 'flat()' methods into one operation. It first maps each element using a mapping function, then flattens the result into a new array. It is useful for applying a function to each element and then flattening the result.

Syntax:
array.flatMap(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that produces an element of the new array, with each element mapped by the provided callback function. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'flatMap()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'flatMap()' method returns a new array with the mapped and flattened elements.

Examples:
1. Mapping and flattening array elements:
let words = ['hello', 'world'];
let mappedAndFlattened = words.flatMap((word) => word.split(''));
console.log(mappedAndFlattened); // Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

2. Mapping and flattening with a function returning arrays:
let numbers = [1, 2, 3, 4];
let mappedAndFlattened = numbers.flatMap((num) => [num * 2, num * 3]);
console.log(mappedAndFlattened); // Output: [2, 3, 4, 6, 6, 9, 8, 12]
""",
        'example': """
            // Example 1:
            let words = ['hello', 'world'];
            let mappedAndFlattened = words.flatMap((word) => word.split(''));
            console.log(mappedAndFlattened); // Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

            // Example 2:
            let numbers = [1, 2, 3, 4];
            let mappedAndFlattened = numbers.flatMap((num) => [num * 2, num * 3]);
            console.log(mappedAndFlattened); // Output: [2, 3, 4, 6, 6, 9, 8, 12]
        """
    },
    {
        'name': 'includes',
        'define': """The 'includes()' method determines whether an array includes a certain value. It returns 'true' if the array contains the value; otherwise, it returns 'false'. The method performs a strict equality comparison (===) for the search.

Syntax:
array.includes(searchElement[, fromIndex])

Parameters:
- 'searchElement' (required): The element to search for in the array.
- 'fromIndex' (optional): The index to start the search from. If not provided, the search starts from index 0.

Return Value:
The 'includes()' method returns 'true' if the array contains the specified element; otherwise, it returns 'false'.

Examples:
1. Checking if an array includes an element:
let fruits = ['apple', 'orange', 'banana'];
let includesOrange = fruits.includes('orange');
console.log(includesOrange); // Output: true

2. Checking from a specific index:
let numbers = [1, 2, 3, 4, 5];
let includes3 = numbers.includes(3, 2);
console.log(includes3); // Output: true

3. Checking for NaN:
let values = [1, NaN, 3];
let includesNaN = values.includes(NaN);
console.log(includesNaN); // Output: true
""",
        'example': """
            // Example 1:
            let fruits = ['apple', 'orange', 'banana'];
            let includesOrange = fruits.includes('orange');
            console.log(includesOrange); // Output: true

            // Example 2:
            let numbers = [1, 2, 3, 4, 5];
            let includes3 = numbers.includes(3, 2);
            console.log(includes3); // Output: true

            // Example 3:
            let values = [1, NaN, 3];
            let includesNaN = values.includes(NaN);
            console.log(includesNaN); // Output: true
        """
    },
    {
        'name': 'indexOf',
        'trigger': 'index of',
        'define': """The 'indexOf()' method returns the first index at which a given element can be found in the array or -1 if it is not present. The method performs a strict equality comparison (===) for the search.

Syntax:
array.indexOf(searchElement[, fromIndex])

Parameters:
- 'searchElement' (required): The element to search for in the array.
- 'fromIndex' (optional): The index to start the search from. If not provided, the search starts from index 0.

Return Value:
The 'indexOf()' method returns the first index at which the specified element is found in the array; otherwise, it returns -1.

Examples:
1. Finding the index of an element in an array:
let numbers = [1, 2, 3, 4, 3, 5];
let index = numbers.indexOf(3);
console.log(index); // Output: 2 (index of the first occurrence of 3)

2. Finding the index from a specific starting point:
let numbers = [1, 2, 3, 4, 3, 5];
let index = numbers.indexOf(3, 3);
console.log(index); // Output: 4 (index of the first occurrence of 3 from index 3)

3. Searching for a non-existent element:
let fruits = ['apple', 'orange', 'banana'];
let index = fruits.indexOf('grape');
console.log(index); // Output: -1 (element 'grape' is not found)
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 3, 5];
            let index = numbers.indexOf(3);
            console.log(index); // Output: 2 (index of the first occurrence of 3)

            // Example 2:
            let numbers = [1, 2, 3, 4, 3, 5];
            let index = numbers.indexOf(3, 3);
            console.log(index); // Output: 4 (index of the first occurrence of 3 from index 3)

            // Example 3:
            let fruits = ['apple', 'orange', 'banana'];
            let index = fruits.indexOf('grape');
            console.log(index); // Output: -1 (element 'grape' is not found)
        """
    },
    {
        'name': 'join',
        'define': """The 'join()' method creates and returns a new string by concatenating all elements in an array using a specified separator. By default, the separator is a comma (','), but it can be customized.

Syntax:
array.join([separator])

Parameters:
- 'separator' (optional): The string used to separate the array elements in the resulting string. If not provided, a comma (',') is used as the default separator.

Return Value:
The 'join()' method returns a new string containing all array elements joined by the specified separator.

Examples:
1. Joining elements of an array with a default separator:
let fruits = ['apple', 'orange', 'banana'];
let result = fruits.join();
console.log(result); // Output: 'apple,orange,banana'

2. Joining elements with a custom separator:
let numbers = [1, 2, 3, 4, 5];
let result = numbers.join('-');
console.log(result); // Output: '1-2-3-4-5'
""",
        'example': """
            // Example 1:
            let fruits = ['apple', 'orange', 'banana'];
            let result = fruits.join();
            console.log(result); // Output: 'apple,orange,banana'

            // Example 2:
            let numbers = [1, 2, 3, 4, 5];
            let result = numbers.join('-');
            console.log(result); // Output: '1-2-3-4-5'
        """
    },
    {
        'name': 'keys',
        'define': """The 'keys()' method returns a new Array Iterator object that contains the keys (indices) of each element in the array. It is used to iterate over the indices of an array.

Syntax:
array.keys()

Return Value:
The 'keys()' method returns a new Array Iterator object.

Examples:
1. Using 'keys()' to iterate over array indices:
let fruits = ['apple', 'orange', 'banana'];
let keysIterator = fruits.keys();
for (let key of keysIterator) {
    console.log(key); // Output: 0, 1, 2
}

2. Converting the Array Iterator to an array:
let fruits = ['apple', 'orange', 'banana'];
let keysIterator = fruits.keys();
let keysArray = Array.from(keysIterator);
console.log(keysArray); // Output: [0, 1, 2]
""",
        'example': """
            // Example 1:
            let fruits = ['apple', 'orange', 'banana'];
            let keysIterator = fruits.keys();
            for (let key of keysIterator) {
                console.log(key); // Output: 0, 1, 2
            }

            // Example 2:
            let fruits = ['apple', 'orange', 'banana'];
            let keysIterator = fruits.keys();
            let keysArray = Array.from(keysIterator);
            console.log(keysArray); // Output: [0, 1, 2]
        """
    },
    {
        'name': 'lastIndexOf',
        'trigger': 'last index',
        'define': """The 'lastIndexOf()' method returns the last index at which a given element can be found in the array or -1 if it is not present. The method performs a strict equality comparison (===) for the search.

Syntax:
array.lastIndexOf(searchElement[, fromIndex])

Parameters:
- 'searchElement' (required): The element to search for in the array.
- 'fromIndex' (optional): The index to start the search from. If not provided, the search starts from the last element of the array.

Return Value:
The 'lastIndexOf()' method returns the last index at which the specified element is found in the array; otherwise, it returns -1.

Examples:
1. Finding the last index of an element in an array:
let numbers = [1, 2, 3, 4, 3, 5];
let lastIndex = numbers.lastIndexOf(3);
console.log(lastIndex); // Output: 4 (last index of 3)

2. Finding the last index from a specific starting point:
let numbers = [1, 2, 3, 4, 3, 5];
let lastIndex = numbers.lastIndexOf(3, 3);
console.log(lastIndex); // Output: 2 (last index of 3 from index 3)

3. Searching for a non-existent element:
let fruits = ['apple', 'orange', 'banana'];
let lastIndex = fruits.lastIndexOf('grape');
console.log(lastIndex); // Output: -1 (element 'grape' is not found)
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 3, 5];
            let lastIndex = numbers.lastIndexOf(3);
            console.log(lastIndex); // Output: 4 (last index of 3)

            // Example 2:
            let numbers = [1, 2, 3, 4, 3, 5];
            let lastIndex = numbers.lastIndexOf(3, 3);
            console.log(lastIndex); // Output: 2 (last index of 3 from index 3)

            // Example 3:
            let fruits = ['apple', 'orange', 'banana'];
            let lastIndex = fruits.lastIndexOf('grape');
            console.log(lastIndex); // Output: -1 (element 'grape' is not found)
        """
    },
    {
        'name': 'map',
        'define': """The 'map()' method creates a new array with the results of calling a provided function on every element in the calling array. It is a higher-order function used for transforming array elements.

Syntax:
array.map(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that produces an element of the new array, with each element in the original array mapped by the provided callback function. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'map()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'map()' method returns a new array with the results of the provided callback function applied to each element of the calling array.

Examples:
1. Mapping each element to its square:
let numbers = [1, 2, 3, 4, 5];
let squaredNumbers = numbers.map((num) => num * num);
console.log(squaredNumbers); // Output: [1, 4, 9, 16, 25]

2. Mapping an array of objects:
let people = [
    { name: 'Alice', age: 30 },
    { name: 'Bob', age: 25 },
    { name: 'Charlie', age: 35 },
];
let names = people.map((person) => person.name);
console.log(names); // Output: ['Alice', 'Bob', 'Charlie']
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let squaredNumbers = numbers.map((num) => num * num);
            console.log(squaredNumbers); // Output: [1, 4, 9, 16, 25]

            // Example 2:
            let people = [
                { name: 'Alice', age: 30 },
                { name: 'Bob', age: 25 },
                { name: 'Charlie', age: 35 },
            ];
            let names = people.map((person) => person.name);
            console.log(names); // Output: ['Alice', 'Bob', 'Charlie']
        """
    },
    {
        'name': 'pop',
        'define': """The 'pop()' method removes the last element from an array and returns that element. This method changes the length of the array.

Syntax:
array.pop()

Return Value:
The 'pop()' method returns the removed element from the array. If the array is empty, 'undefined' is returned.

Examples:
1. Removing the last element from an array:
let numbers = [1, 2, 3, 4, 5];
let removedElement = numbers.pop();
console.log(numbers); // Output: [1, 2, 3, 4]
console.log(removedElement); // Output: 5

2. Removing the last element from an empty array:
let emptyArray = [];
let removedElement = emptyArray.pop();
console.log(emptyArray); // Output: []
console.log(removedElement); // Output: undefined
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let removedElement = numbers.pop();
            console.log(numbers); // Output: [1, 2, 3, 4]
            console.log(removedElement); // Output: 5

            // Example 2:
            let emptyArray = [];
            let removedElement = emptyArray.pop();
            console.log(emptyArray); // Output: []
            console.log(removedElement); // Output: undefined
        """
    },
    {
        'name': 'push',
        'define': """The 'push()' method adds one or more elements to the end of an array and returns the new length of the array.

Syntax:
array.push(element1[, element2[, ...[, elementN]]])

Parameters:
- 'element1' (required): The first element to add to the end of the array.
- 'element2', 'element3', ..., 'elementN' (optional): Additional elements to add to the end of the array.

Return Value:
The 'push()' method returns the new length of the array after adding the specified elements.

Examples:
1. Adding elements to the end of an array:
let numbers = [1, 2, 3];
let newLength = numbers.push(4, 5);
console.log(numbers); // Output: [1, 2, 3, 4, 5]
console.log(newLength); // Output: 5

2. Adding elements to an empty array:
let emptyArray = [];
let newLength = emptyArray.push('a', 'b', 'c');
console.log(emptyArray); // Output: ['a', 'b', 'c']
console.log(newLength); // Output: 3
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3];
            let newLength = numbers.push(4, 5);
            console.log(numbers); // Output: [1, 2, 3, 4, 5]
            console.log(newLength); // Output: 5

            // Example 2:
            let emptyArray = [];
            let newLength = emptyArray.push('a', 'b', 'c');
            console.log(emptyArray); // Output: ['a', 'b', 'c']
            console.log(newLength); // Output: 3
        """
    },
    {
        'name': 'reduce',
        'define': """The 'reduce()' method executes a reducer function on each element of the array, resulting in a single output value. It is often used for calculating the cumulative result of array elements.

Syntax:
array.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])

Parameters:
- 'callback' (required): A function that is called for each element in the array. It takes four arguments:
    - 'accumulator': The accumulated result from previous iterations. It is the value returned from the previous invocation of the callback function.
    - 'currentValue': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'reduce()' was called.
- 'initialValue' (optional): A value used as the initial value for the 'accumulator' in the first call to the callback function.

Return Value:
The 'reduce()' method returns the final accumulated value.

Examples:
1. Summing all elements in an array:
let numbers = [1, 2, 3, 4, 5];
let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
console.log(sum); // Output: 15

2. Calculating the product of all elements:
let numbers = [2, 3, 4];
let product = numbers.reduce((accumulator, currentValue) => accumulator * currentValue);
console.log(product); // Output: 24
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
            console.log(sum); // Output: 15

            // Example 2:
            let numbers = [2, 3, 4];
            let product = numbers.reduce((accumulator, currentValue) => accumulator * currentValue);
            console.log(product); // Output: 24
        """
    },
    {
        'name': 'reduceRight',
        'trigger': 'reduce right',
        'define': """The 'reduceRight()' method is similar to 'reduce()', but it executes the reducer function starting from the last element towards the first element of the array.

Syntax:
array.reduceRight(callback(accumulator, currentValue[, index[, array]])[, initialValue])

Parameters:
- 'callback' (required): A function that is called for each element in the array, starting from the last element to the first. It takes four arguments:
    - 'accumulator': The accumulated result from previous iterations. It is the value returned from the previous invocation of the callback function.
    - 'currentValue': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'reduceRight()' was called.
- 'initialValue' (optional): A value used as the initial value for the 'accumulator' in the first call to the callback function.

Return Value:
The 'reduceRight()' method returns the final accumulated value.

Examples:
1. Concatenating array elements in reverse order:
let fruits = ['apple', 'orange', 'banana'];
let reversedString = fruits.reduceRight((accumulator, currentValue) => accumulator + ' ' + currentValue);
console.log(reversedString); // Output: 'banana orange apple'
""",
        'example': """
            // Example 1:
            let fruits = ['apple', 'orange', 'banana'];
            let reversedString = fruits.reduceRight((accumulator, currentValue) => accumulator + ' ' + currentValue);
            console.log(reversedString); // Output: 'banana orange apple'
        """
    },
    {
        'name': 'reverse',
        'define': """The 'reverse()' method reverses the order of the elements in an array. The first element becomes the last, and the last element becomes the first.

Syntax:
array.reverse()

Return Value:
The 'reverse()' method modifies the original array and returns the reversed array. It does not create a new array.

Examples:
1. Reversing an array:
let numbers = [1, 2, 3, 4, 5];
numbers.reverse();
console.log(numbers); // Output: [5, 4, 3, 2, 1]

2. Reversing an array of strings:
let colors = ['red', 'green', 'blue'];
colors.reverse();
console.log(colors); // Output: ['blue', 'green', 'red']
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            numbers.reverse();
            console.log(numbers); // Output: [5, 4, 3, 2, 1]

            // Example 2:
            let colors = ['red', 'green', 'blue'];
            colors.reverse();
            console.log(colors); // Output: ['blue', 'green', 'red']
        """
    },
    {
        'name': 'shift',
        'define': """The 'shift()' method removes the first element from an array and returns that element. This method changes the length of the array.

Syntax:
array.shift()

Return Value:
The 'shift()' method returns the removed element from the array. If the array is empty, 'undefined' is returned.

Examples:
1. Removing the first element from an array:
let numbers = [1, 2, 3, 4, 5];
let removedElement = numbers.shift();
console.log(numbers); // Output: [2, 3, 4, 5]
console.log(removedElement); // Output: 1

2. Removing the first element from an empty array:
let emptyArray = [];
let removedElement = emptyArray.shift();
console.log(emptyArray); // Output: []
console.log(removedElement); // Output: undefined
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let removedElement = numbers.shift();
            console.log(numbers); // Output: [2, 3, 4, 5]
            console.log(removedElement); // Output: 1

            // Example 2:
            let emptyArray = [];
            let removedElement = emptyArray.shift();
            console.log(emptyArray); // Output: []
            console.log(removedElement); // Output: undefined
        """
    },
    {
        'name': 'slice',
        'define': """The 'slice()' method extracts a section of an array and returns a new array containing the selected elements. It does not modify the original array.

Syntax:
array.slice([start[, end]])

Parameters:
- 'start' (optional): The beginning index of the extraction. If 'start' is undefined, 'slice()' will start from index 0. A negative 'start' index can be used to specify an offset from the end of the array.
- 'end' (optional): The ending index of the extraction. 'slice()' extracts elements up to, but not including, 'end'. If 'end' is omitted, 'slice()' extracts elements up to the end of the array. A negative 'end' index can be used to specify an offset from the end of the array.

Return Value:
The 'slice()' method returns a new array containing the extracted elements. If 'start' is greater than or equal to the length of the array, an empty array is returned.

Examples:
1. Slicing elements from an array:
let numbers = [1, 2, 3, 4, 5];
let slicedNumbers = numbers.slice(1, 4);
console.log(slicedNumbers); // Output: [2, 3, 4]

2. Slicing elements with negative indices:
let numbers = [1, 2, 3, 4, 5];
let slicedNumbers = numbers.slice(-3, -1);
console.log(slicedNumbers); // Output: [3, 4]
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let slicedNumbers = numbers.slice(1, 4);
            console.log(slicedNumbers); // Output: [2, 3, 4]

            // Example 2:
            let numbers = [1, 2, 3, 4, 5];
            let slicedNumbers = numbers.slice(-3, -1);
            console.log(slicedNumbers); // Output: [3, 4]
        """
    },
    {
        'name': 'some',
        'define': """The 'some()' method tests whether at least one element in the array passes the test implemented by the provided callback function. It returns 'true' if any element satisfies the condition, otherwise 'false'.

Syntax:
array.some(callback(element[, index[, array]])[, thisArg])

Parameters:
- 'callback' (required): A function that tests each element of the array. It takes three arguments:
    - 'element': The current element being processed in the array.
    - 'index' (optional): The index of the current element in the array.
    - 'array' (optional): The array on which 'some()' was called.
- 'thisArg' (optional): An object to use as 'this' when executing the callback function.

Return Value:
The 'some()' method returns 'true' if the callback function returns 'true' for at least one element in the array; otherwise, it returns 'false'.

Examples:
1. Checking if any element is greater than 3:
let numbers = [1, 2, 3, 4, 5];
let hasGreaterThanThree = numbers.some((num) => num > 3);
console.log(hasGreaterThanThree); // Output: true

2. Checking for even numbers:
let numbers = [1, 2, 3, 4, 5];
let hasEvenNumber = numbers.some((num) => num % 2 === 0);
console.log(hasEvenNumber); // Output: true

3. Using 'thisArg' to check for a threshold:
let threshold = 10;
let values = [5, 15, 25];
let hasThresholdValue = values.some(function (value) {
    return value >= this.threshold;
}, { threshold });
console.log(hasThresholdValue); // Output: true
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let hasGreaterThanThree = numbers.some((num) => num > 3);
            console.log(hasGreaterThanThree); // Output: true

            // Example 2:
            let numbers = [1, 2, 3, 4, 5];
            let hasEvenNumber = numbers.some((num) => num % 2 === 0);
            console.log(hasEvenNumber); // Output: true

            // Example 3:
            let threshold = 10;
            let values = [5, 15, 25];
            let hasThresholdValue = values.some(function (value) {
                return value >= this.threshold;
            }, { threshold });
            console.log(hasThresholdValue); // Output: true
        """
    },
    {
        'name': 'sort',
        'define': """The 'sort()' method sorts the elements of an array in place and returns the sorted array. The default sort order is lexicographic (string-based) ascending. It modifies the original array and does not create a new one.

Syntax:
array.sort([compareFunction])

Parameters:
- 'compareFunction' (optional): A function that defines the sort order. If omitted, the array elements are converted to strings and sorted based on their UTF-16 code units. The compare function should return a negative value if 'a' should come before 'b', a positive value if 'a' should come after 'b', or 0 if 'a' and 'b' are considered equal.

Return Value:
The 'sort()' method returns the sorted array. Note that the original array is also modified.

Examples:
1. Sorting an array of numbers in ascending order:
let numbers = [3, 1, 4, 2, 5];
numbers.sort();
console.log(numbers); // Output: [1, 2, 3, 4, 5]

2. Sorting an array of strings in alphabetical order:
let fruits = ['banana', 'orange', 'apple'];
fruits.sort();
console.log(fruits); // Output: ['apple', 'banana', 'orange']

3. Sorting an array of objects based on a property:
let people = [
    { name: 'Alice', age: 30 },
    { name: 'Bob', age: 25 },
    { name: 'Charlie', age: 35 },
];
people.sort((a, b) => a.age - b.age);
console.log(people);
// Output: [
//   { name: 'Bob', age: 25 },
//   { name: 'Alice', age: 30 },
//   { name: 'Charlie', age: 35 }
// ]
""",
        'example': """
            // Example 1:
            let numbers = [3, 1, 4, 2, 5];
            numbers.sort();
            console.log(numbers); // Output: [1, 2, 3, 4, 5]

            // Example 2:
            let fruits = ['banana', 'orange', 'apple'];
            fruits.sort();
            console.log(fruits); // Output: ['apple', 'banana', 'orange']

            // Example 3:
            let people = [
                { name: 'Alice', age: 30 },
                { name: 'Bob', age: 25 },
                { name: 'Charlie', age: 35 },
            ];
            people.sort((a, b) => a.age - b.age);
            console.log(people);
            // Output: [
            //   { name: 'Bob', age: 25 },
            //   { name: 'Alice', age: 30 },
            //   { name: 'Charlie', age: 35 }
            // ]
        """
    },
    {
        'name': 'splice',
        'define': """The 'splice()' method changes the content of an array by removing or replacing existing elements and/or adding new elements in place. It modifies the original array and returns an array containing the removed elements, if any.

Syntax:
array.splice(start[, deleteCount[, item1[, item2[, ...]]]])

Parameters:
- 'start' (required): The index at which to start changing the array. If negative, it specifies an offset from the end of the array.
- 'deleteCount' (optional): The number of elements to remove from the array. If 'deleteCount' is 0, no elements are removed. If 'deleteCount' is not provided, all elements from 'start' to the end of the array will be removed.
- 'item1', 'item2', ... (optional): The elements to add to the array, beginning at the 'start' index. If no elements are specified, 'splice()' will only remove elements.

Return Value:
The 'splice()' method returns an array containing the elements that were removed. If no elements are removed, an empty array is returned.

Examples:
1. Removing elements from an array:
let numbers = [1, 2, 3, 4, 5];
let removedElements = numbers.splice(1, 2);
console.log(numbers); // Output: [1, 4, 5]
console.log(removedElements); // Output: [2, 3]

2. Replacing elements in an array:
let colors = ['red', 'green', 'blue'];
let replacedElements = colors.splice(1, 1, 'yellow', 'orange');
console.log(colors); // Output: ['red', 'yellow', 'orange', 'blue']
console.log(replacedElements); // Output: ['green']
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];
            let removedElements = numbers.splice(1, 2);
            console.log(numbers); // Output: [1, 4, 5]
            console.log(removedElements); // Output: [2, 3]

            // Example 2:
            let colors = ['red', 'green', 'blue'];
            let replacedElements = colors.splice(1, 1, 'yellow', 'orange');
            console.log(colors); // Output: ['red', 'yellow', 'orange', 'blue']
            console.log(replacedElements); // Output: ['green']
        """
    },
    {
        'name': 'toLocaleString',
        'trigger': 'locale string',
        'define': """The 'toLocaleString()' method returns a string representing the elements of an array. The elements are converted to strings using their 'toLocaleString()' methods and then concatenated into a single string. This method does not modify the original array.

Syntax:
array.toLocaleString([locales[, options]])

Parameters:
- 'locales' (optional): A string with a BCP 47 language tag or an array of such strings, indicating the language(s) to be used for formatting. If not provided, the default locale of the JavaScript runtime is used.
- 'options' (optional): An object with configuration options. It can have properties like 'style' (e.g., 'decimal', 'currency', 'percent') and 'currency' (e.g., 'USD', 'EUR') to customize the formatting.

Return Value:
The 'toLocaleString()' method returns a string representing the elements of the array.

Examples:
1. Converting an array to a localized string:
let numbers = [1000, 2000, 3000];
let localizedString = numbers.toLocaleString();
console.log(localizedString); // Output: '1,000,2,000,3,000'

2. Using locales and options for formatting:
let numbers = [1000, 2000, 3000];
let localizedString = numbers.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' });
console.log(localizedString); // Output: '1.000,00 €,2.000,00 €,3.000,00 €'
""",
        'example': """
            // Example 1:
            let numbers = [1000, 2000, 3000];
            let localizedString = numbers.toLocaleString();
            console.log(localizedString); // Output: '1,000,2,000,3,000'

            // Example 2:
            let numbers = [1000, 2000, 3000];
            let localizedString = numbers.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' });
            console.log(localizedString); // Output: '1.000,00 €,2.000,00 €,3.000,00 €'
        """
    },
    {
        'name': 'toString',
        'trigger': 'to string',
        'define': """The 'toString()' method returns a string representing the specified array and its elements. The elements are converted to strings using their 'toString()' methods and separated by commas. This method does not modify the original array.

Syntax:
array.toString()

Return Value:
The 'toString()' method returns a string representation of the array.

Examples:
1. Converting an array to a comma-separated string:
let fruits = ['apple', 'banana', 'orange'];
let fruitsString = fruits.toString();
console.log(fruitsString); // Output: 'apple,banana,orange'

2. Converting an array of numbers to a string:
let numbers = [1, 2, 3, 4, 5];
let numbersString = numbers.toString();
console.log(numbersString); // Output: '1,2,3,4,5'
""",
        'example': """
            // Example 1:
            let fruits = ['apple', 'banana', 'orange'];
            let fruitsString = fruits.toString();
            console.log(fruitsString); // Output: 'apple,banana,orange'

            // Example 2:
            let numbers = [1, 2, 3, 4, 5];
            let numbersString = numbers.toString();
            console.log(numbersString); // Output: '1,2,3,4,5'
        """
    },
    {
        'name': 'unshift',
        'define': """The 'unshift()' method adds one or more elements to the beginning of an array and returns the new length of the array.

Syntax:
array.unshift(element1[, element2[, ...[, elementN]]])

Parameters:
- 'element1', 'element2', ..., 'elementN' (required): The elements to add to the beginning of the array.

Return Value:
The 'unshift()' method returns the new length of the array after adding the specified elements.

Examples:
1. Adding elements to the beginning of an array:
let numbers = [3, 4, 5];
let newLength = numbers.unshift(1, 2);
console.log(numbers); // Output: [1, 2, 3, 4, 5]
console.log(newLength); // Output: 5

2. Adding elements to an empty array:
let emptyArray = [];
let newLength = emptyArray.unshift('a', 'b', 'c');
console.log(emptyArray); // Output: ['a', 'b', 'c']
console.log(newLength); // Output: 3
""",
        'example': """
            // Example 1:
            let numbers = [3, 4, 5];
            let newLength = numbers.unshift(1, 2);
            console.log(numbers); // Output: [1, 2, 3, 4, 5]
            console.log(newLength); // Output: 5

            // Example 2:
            let emptyArray = [];
            let newLength = emptyArray.unshift('a', 'b', 'c');
            console.log(emptyArray); // Output: ['a', 'b', 'c']
            console.log(newLength); // Output: 3
        """
    },
    {
        'name': 'valueOf',
        'trigger': 'value of',
        'define': """The 'valueOf()' method returns the primitive value of an array, which is the same as calling 'array.toString()'. This method is called automatically when an array is used in a context where a primitive value is expected, such as when an array is concatenated with a string.

Syntax:
array.valueOf()

Return Value:
The 'valueOf()' method returns a primitive value (a string) representing the array.

Examples:
1. Using 'valueOf()' to get the primitive value of an array:
let numbers = [1, 2, 3];
let primitiveValue = numbers.valueOf();
console.log(primitiveValue); // Output: '1,2,3'

2. Implicitly calling 'valueOf()' in a string context:
let fruits = ['apple', 'banana'];
let message = 'I like ' + fruits;
console.log(message); // Output: 'I like apple,banana'
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3];
            let primitiveValue = numbers.valueOf();
            console.log(primitiveValue); // Output: '1,2,3'

            // Example 2:
            let fruits = ['apple', 'banana'];
            let message = 'I like ' + fruits;
            console.log(message); // Output: 'I like apple,banana'
        """
    },
    {
        'name': 'Set',
        'define': """The 'Set' object is a collection of unique values, meaning that each value can only occur once in the collection. It provides a simple way to create a list of distinct values, and it can store values of any data type, including objects.

Syntax (Creating a Set):
new Set([iterable])

Parameters:
- 'iterable' (optional): An iterable object (e.g., an array) whose elements will be added to the new Set. If not provided or 'null', an empty Set will be created.

Return Value:
A new Set object containing the unique elements from the provided iterable.

Examples:
1. Creating a Set from an array:
let numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5];
let uniqueNumbers = new Set(numbers);
console.log(uniqueNumbers); // Output: Set { 1, 2, 3, 4, 5 }

2. Creating a Set with mixed data types:
let mixedData = [1, 'apple', { name: 'John' }, 'apple', { name: 'John' }, true, false];
let uniqueData = new Set(mixedData);
console.log(uniqueData);
// Output: Set { 1, 'apple', { name: 'John' }, true, false }
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5];
            let uniqueNumbers = new Set(numbers);
            console.log(uniqueNumbers); // Output: Set { 1, 2, 3, 4, 5 }

            // Example 2:
            let mixedData = [1, 'apple', { name: 'John' }, 'apple', { name: 'John' }, true, false];
            let uniqueData = new Set(mixedData);
            console.log(uniqueData);
            // Output: Set { 1, 'apple', { name: 'John' }, true, false }
        """
    },
    {
        'name': 'WeakSet',
        'trigger': 'weak set',
        'define': """The 'WeakSet' object is a collection of weakly held objects. Unlike 'Set', it can only contain objects, and these objects are held weakly, meaning they can be garbage-collected if there are no other strong references to them. It is often used to store a set of objects without preventing them from being garbage-collected.

Syntax (Creating a WeakSet):
new WeakSet([iterable])

Parameters:
- 'iterable' (optional): An iterable object (e.g., an array) whose elements (objects) will be added to the new WeakSet. If not provided or 'null', an empty WeakSet will be created.

Return Value:
A new WeakSet object containing the elements (objects) from the provided iterable.

Note: Due to weak references, there is no list of elements or method to loop over the elements of a WeakSet.

Example:
1. Creating a WeakSet with objects:
let john = { name: 'John' };
let jane = { name: 'Jane' };
let weakSet = new WeakSet([john, jane]);
console.log(weakSet); // Output: WeakSet { [items unknown] }
""",
        'example': """
            // Example 1:
            let john = { name: 'John' };
            let jane = { name: 'Jane' };
            let weakSet = new WeakSet([john, jane]);
            console.log(weakSet); // Output: WeakSet { [items unknown] }
        """
    },
    {
        'name': 'Map',
        'define': """The 'Map' object is a collection of key-value pairs where each key can occur only once in the Map. It provides a way to store and retrieve data based on keys and is often used to associate values with specific identifiers.

Syntax (Creating a Map):
new Map([iterable])

Parameters:
- 'iterable' (optional): An iterable object (e.g., an array) whose elements are key-value pairs (arrays with two elements) to be added to the new Map. If not provided or 'null', an empty Map will be created.

Return Value:
A new Map object containing the key-value pairs from the provided iterable.

Examples:
1. Creating a Map from an array of key-value pairs:
let keyValuePairs = [['a', 1], ['b', 2], ['c', 3]];
let map = new Map(keyValuePairs);
console.log(map);
// Output: Map { 'a' => 1, 'b' => 2, 'c' => 3 }

2. Creating a Map with various data types as keys and values:
let complexMap = new Map();
let objKey = { name: 'John' };
let funcKey = function () {};
let symKey = Symbol('key');
complexMap.set(objKey, 'Value for object key');
complexMap.set(funcKey, 'Value for function key');
complexMap.set(symKey, 'Value for symbol key');
console.log(complexMap);
// Output: Map { { name: 'John' } => 'Value for object key', [Function (anonymous)] => 'Value for function key', Symbol(key) => 'Value for symbol key' }
""",
        'example': """
            // Example 1:
            let keyValuePairs = [['a', 1], ['b', 2], ['c', 3]];
            let map = new Map(keyValuePairs);
            console.log(map);
            // Output: Map { 'a' => 1, 'b' => 2, 'c' => 3 }

            // Example 2:
            let complexMap = new Map();
            let objKey = { name: 'John' };
            let funcKey = function () {};
            let symKey = Symbol('key');
            complexMap.set(objKey, 'Value for object key');
            complexMap.set(funcKey, 'Value for function key');
            complexMap.set(symKey, 'Value for symbol key');
            console.log(complexMap);
            // Output: Map { { name: 'John' } => 'Value for object key', [Function (anonymous)] => 'Value for function key', Symbol(key) => 'Value for symbol key' }
        """
    },
    {
        'name': 'WeakMap',
        'trigger': 'weak map',
        'define': """The 'WeakMap' object is a collection of weakly held key-value pairs, where keys must be objects. Similar to 'WeakSet', keys in a 'WeakMap' are held weakly, meaning they can be garbage-collected if there are no other strong references to them. It is often used to store private data associated with specific objects.

Syntax (Creating a WeakMap):
new WeakMap([iterable])

Parameters:
- 'iterable' (optional): An iterable object (e.g., an array) whose elements are key-value pairs (arrays with two elements) to be added to the new WeakMap. If not provided or 'null', an empty WeakMap will be created.

Return Value:
A new WeakMap object containing the key-value pairs from the provided iterable.

Example:
1. Creating a WeakMap with objects as keys:
let john = { name: 'John' };
let jane = { name: 'Jane' };
let weakMap = new WeakMap([[john, 'John Doe'], [jane, 'Jane Doe']]);
console.log(weakMap); // Output: WeakMap { [items unknown] }
""",
        'example': """
            // Example 1:
            let john = { name: 'John' };
            let jane = { name: 'Jane' };
            let weakMap = new WeakMap([[john, 'John Doe'], [jane, 'Jane Doe']]);
            console.log(weakMap); // Output: WeakMap { [items unknown] }
        """
    },
    {
        'name': 'JSON',
        'define': """JSON (JavaScript Object Notation) is a lightweight data-interchange format used for data exchange between a server and a client, as well as for storing and transmitting structured data. It is based on a subset of the JavaScript language and is language-independent, meaning it can be used with most modern programming languages.

In JavaScript, the 'JSON' object provides methods for working with JSON data, including parsing JSON strings and converting JavaScript objects to JSON strings.

Example (Parsing a JSON string):
let jsonString = '{"name": "John", "age": 30, "city": "New York"}';
let parsedObject = JSON.parse(jsonString);
console.log(parsedObject);
// Output: { name: 'John', age: 30, city: 'New York' }

Example (Converting a JavaScript object to a JSON string):
let person = { name: 'Alice', age: 25, city: 'London' };
let jsonString = JSON.stringify(person);
console.log(jsonString);
// Output: '{"name":"Alice","age":25,"city":"London"}'
""",
        'example': """
            // Example (Parsing a JSON string):
            let jsonString = '{"name": "John", "age": 30, "city": "New York"}';
            let parsedObject = JSON.parse(jsonString);
            console.log(parsedObject);
            // Output: { name: 'John', age: 30, city: 'New York' }

            // Example (Converting a JavaScript object to a JSON string):
            let person = { name: 'Alice', age: 25, city: 'London' };
            let jsonString = JSON.stringify(person);
            console.log(jsonString);
            // Output: '{"name":"Alice","age":25,"city":"London"}'
        """
    },
    {
        'name': 'Promise',
        'define': """A 'Promise' is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value. It allows you to handle asynchronous operations more easily by chaining methods to handle success or failure. A Promise can be in one of three states: 'pending', 'fulfilled', or 'rejected'.

Syntax (Creating a Promise):
new Promise(executor)

Parameters:
- 'executor' (required): A function with two arguments, 'resolve' and 'reject'. It contains the asynchronous operation, which, when successful, calls 'resolve(value)' with the result value, and when it fails, calls 'reject(reason)' with an error or reason for the failure.

Example:
1. Creating and using a Promise to simulate an asynchronous operation:
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let randomNum = Math.random();
        if (randomNum < 0.5) {
            resolve(randomNum);
        } else {
            reject('Error: Random number is greater than or equal to 0.5');
        }
    }, 1000);
});

promise.then(
    (result) => console.log('Fulfilled:', result),
    (error) => console.log('Rejected:', error)
);
""",
        'example': """
            // Example 1:
            let promise = new Promise((resolve, reject) => {
                setTimeout(() => {
                    let randomNum = Math.random();
                    if (randomNum < 0.5) {
                        resolve(randomNum);
                    } else {
                        reject('Error: Random number is greater than or equal to 0.5');
                    }
                }, 1000);
            });

            promise.then(
                (result) => console.log('Fulfilled:', result),
                (error) => console.log('Rejected:', error)
            );
        """
    },
    {
        'name': 'async/await',
        'trigger': 'await',
        'define': """'async/await' is a modern way of handling asynchronous operations in JavaScript. It allows you to write asynchronous code that looks more like synchronous code, making it easier to reason about and maintain.

The 'async' keyword is used to define an asynchronous function, and the 'await' keyword is used to pause the execution of the function until an asynchronous operation completes. When using 'await', the function will wait for the promise to resolve and then return the resolved value or throw an error if the promise is rejected.

Example:
1. Using 'async/await' to handle asynchronous operations:
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Data received'), 2000);
    });
}

async function getData() {
    try {
        const result = await fetchData();
        console.log(result);
    } catch (error) {
        console.log('Error:', error);
    }
}

getData();
// Output (after 2 seconds): 'Data received'
""",
        'example': """
            // Example 1:
            function fetchData() {
                return new Promise((resolve) => {
                    setTimeout(() => resolve('Data received'), 2000);
                });
            }

            async function getData() {
                try {
                    const result = await fetchData();
                    console.log(result);
                } catch (error) {
                    console.log('Error:', error);
                }
            }

            getData();
            // Output (after 2 seconds): 'Data received'
        """
    },
    {
        'name': 'async/await',
        'trigger': 'async',
        'define': """'async/await' is a modern way of handling asynchronous operations in JavaScript. It allows you to write asynchronous code that looks more like synchronous code, making it easier to reason about and maintain.

The 'async' keyword is used to define an asynchronous function, and the 'await' keyword is used to pause the execution of the function until an asynchronous operation completes. When using 'await', the function will wait for the promise to resolve and then return the resolved value or throw an error if the promise is rejected.

Example:
1. Using 'async/await' to handle asynchronous operations:
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Data received'), 2000);
    });
}

async function getData() {
    try {
        const result = await fetchData();
        console.log(result);
    } catch (error) {
        console.log('Error:', error);
    }
}

getData();
// Output (after 2 seconds): 'Data received'
""",
        'example': """
            // Example 1:
            function fetchData() {
                return new Promise((resolve) => {
                    setTimeout(() => resolve('Data received'), 2000);
                });
            }

            async function getData() {
                try {
                    const result = await fetchData();
                    console.log(result);
                } catch (error) {
                    console.log('Error:', error);
                }
            }

            getData();
            // Output (after 2 seconds): 'Data received'
        """
    },
    {
        'name': 'try',
        'define': """'try/catch' is a control structure in JavaScript used for handling errors and exceptions in synchronous code. The 'try' block contains the code that might throw an error, and the 'catch' block handles the error if it occurs.

If an error is thrown within the 'try' block, the 'catch' block is executed, and the error object is passed as the argument to the 'catch' block.

Syntax:
try {
    // Code that might throw an error
} catch (error) {
    // Code to handle the error
}

Example:
1. Using 'try/catch' to handle a potential error:
function divideNumbers(a, b) {
    try {
        if (b === 0) {
            throw new Error('Division by zero is not allowed.');
        }
        return a / b;
    } catch (error) {
        console.log('Error:', error.message);
        return null;
    }
}

let result1 = divideNumbers(10, 2);
console.log(result1); // Output: 5

let result2 = divideNumbers(8, 0);
console.log(result2); // Output: null
""",
        'example': """
            // Example 1:
            function divideNumbers(a, b) {
                try {
                    if (b === 0) {
                        throw new Error('Division by zero is not allowed.');
                    }
                    return a / b;
                } catch (error) {
                    console.log('Error:', error.message);
                    return null;
                }
            }

            let result1 = divideNumbers(10, 2);
            console.log(result1); // Output: 5

            let result2 = divideNumbers(8, 0);
            console.log(result2); // Output: null
        """
    },
    {
        'name': 'catch',
        'define': """'try/catch' is a control structure in JavaScript used for handling errors and exceptions in synchronous code. The 'try' block contains the code that might throw an error, and the 'catch' block handles the error if it occurs.

If an error is thrown within the 'try' block, the 'catch' block is executed, and the error object is passed as the argument to the 'catch' block.

Syntax:
try {
    // Code that might throw an error
} catch (error) {
    // Code to handle the error
}

Example:
1. Using 'try/catch' to handle a potential error:
function divideNumbers(a, b) {
    try {
        if (b === 0) {
            throw new Error('Division by zero is not allowed.');
        }
        return a / b;
    } catch (error) {
        console.log('Error:', error.message);
        return null;
    }
}

let result1 = divideNumbers(10, 2);
console.log(result1); // Output: 5

let result2 = divideNumbers(8, 0);
console.log(result2); // Output: null
""",
        'example': """
            // Example 1:
            function divideNumbers(a, b) {
                try {
                    if (b === 0) {
                        throw new Error('Division by zero is not allowed.');
                    }
                    return a / b;
                } catch (error) {
                    console.log('Error:', error.message);
                    return null;
                }
            }

            let result1 = divideNumbers(10, 2);
            console.log(result1); // Output: 5

            let result2 = divideNumbers(8, 0);
            console.log(result2); // Output: null
        """
    },
    {
        'name': 'Error',
        'define': """'Error' is a built-in constructor function in JavaScript that creates an error object. When an error occurs during the execution of code, an 'Error' object is thrown with information about the error, including an error message and a stack trace.

Syntax:
new Error([message])

Parameters:
- 'message' (optional): A human-readable description of the error.

Example:
1. Creating and throwing a custom error:
function doSomething() {
    throw new Error('Something went wrong.');
}

try {
    doSomething();
} catch (error) {
    console.log('Error:', error.message);
    console.log('Stack Trace:', error.stack);
}
""",
        'example': """
            // Example 1:
            function doSomething() {
                throw new Error('Something went wrong.');
            }

            try {
                doSomething();
            } catch (error) {
                console.log('Error:', error.message);
                console.log('Stack Trace:', error.stack);
            }
        """
    },
    {
        'name': 'Error Types (e.g., TypeError, ReferenceError)',
        'trigger': 'error types',
        'define': """In JavaScript, 'Error' is a base constructor, and there are several built-in error subclasses that inherit from it. These error subclasses are used to represent specific types of errors that can occur during program execution.

Common Error Types:
1. 'TypeError': This error occurs when a value is not of the expected type. For example, calling a method on an undefined or null value may result in a 'TypeError'.

2. 'ReferenceError': This error occurs when trying to access a variable or function that does not exist or is not in scope.

3. 'SyntaxError': This error occurs when there is a syntax mistake in the code.

4. 'RangeError': This error occurs when a value is not within the allowed range. For example, passing a negative value to 'Array.length' or using an invalid radix in 'parseInt' can result in a 'RangeError'.

5. 'EvalError': This error is thrown when an error occurs during the execution of 'eval()' function.

6. 'URIError': This error is thrown when there is a problem with the URI (Uniform Resource Identifier) handling functions.

Example:
1. Using 'try/catch' to handle different error types:
function divideNumbers(a, b) {
    try {
        if (b === 0) {
            throw new Error('Division by zero is not allowed.');
        }
        return a / b;
    } catch (error) {
        if (error instanceof TypeError) {
            console.log('TypeError:', error.message);
        } else if (error instanceof ReferenceError) {
            console.log('ReferenceError:', error.message);
        } else if (error instanceof RangeError) {
            console.log('RangeError:', error.message);
        } else {
            console.log('Error:', error.message);
        }
        return null;
    }
}
""",
        'example': """
            // Example 1:
            function divideNumbers(a, b) {
                try {
                    if (b === 0) {
                        throw new Error('Division by zero is not allowed.');
                    }
                    return a / b;
                } catch (error) {
                    if (error instanceof TypeError) {
                        console.log('TypeError:', error.message);
                    } else if (error instanceof ReferenceError) {
                        console.log('ReferenceError:', error.message);
                    } else if (error instanceof RangeError) {
                        console.log('RangeError:', error.message);
                    } else {
                        console.log('Error:', error.message);
                    }
                    return null;
                }
            }
        """
    },
    {
        'name': 'finally',
        'define': """'finally' is a block that follows the 'try' and 'catch' blocks in a 'try/catch/finally' statement. It contains code that will be executed regardless of whether an error occurs or not. The 'finally' block is commonly used to perform cleanup actions, such as releasing resources or closing connections.

Syntax:
try {
    // Code that might throw an error
} catch (error) {
    // Code to handle the error
} finally {
    // Code that will be executed regardless of whether there was an error or not
}

Example:
1. Using 'finally' to ensure resource cleanup:
function fetchData() {
    let resource = acquireResource();

    try {
        // Use the resource to fetch data
        return data;
    } catch (error) {
        // Handle the error
    } finally {
        // Always release the resource, even if there was an error
        releaseResource(resource);
    }
}
""",
        'example': """
            // Example 1:
            function fetchData() {
                let resource = acquireResource();

                try {
                    // Use the resource to fetch data
                    return data;
                } catch (error) {
                    // Handle the error
                } finally {
                    // Always release the resource, even if there was an error
                    releaseResource(resource);
                }
            }
        """
    },
    {
        'name': 'Event',
        'define': """In the context of web development, an 'Event' is an occurrence triggered by a user action or by the browser itself. Events can be related to user interactions (e.g., clicking a button) or to changes in the state of the browser or the web page (e.g., page loading, resizing).

JavaScript provides mechanisms to handle events and attach event listeners to elements. Event listeners are functions that are executed when a specific event occurs.

Examples of Common Events:
1. 'click': Triggered when a mouse click occurs on an element.
2. 'keydown': Triggered when a keyboard key is pressed.
3. 'mouseover': Triggered when the mouse pointer moves over an element.
4. 'submit': Triggered when a form is submitted.
5. 'load': Triggered when a web page or an external resource finishes loading.
6. 'resize': Triggered when the browser window is resized.

Example (Adding an event listener for a button click):
HTML:
<button id="myButton">Click Me</button>

JavaScript:
document.getElementById('myButton').addEventListener('click', function() {
    alert('Button clicked!');
});
""",
        'example': """
            // Example 1:
            HTML:
            <button id="myButton">Click Me</button>

            JavaScript:
            document.getElementById('myButton').addEventListener('click', function() {
                alert('Button clicked!');
            });
        """
    },
    {
        'name': 'addEventListener',
        'trigger': 'add event',
        'define': """'addEventListener' is a method used to attach an event listener to an element in the DOM (Document Object Model). It allows you to specify a function that should be executed when a specific event is triggered on the element.

Syntax:
element.addEventListener(event, listenerFunction, options);

Parameters:
- 'event' (required): A string that specifies the name of the event to listen for (e.g., 'click', 'keydown', 'mouseover', etc.).
- 'listenerFunction' (required): The function that will be executed when the specified event occurs.
- 'options' (optional): An object that specifies additional options for the event listener, such as 'once' (true/false) to indicate if the listener should only be triggered once.

Example:
1. Adding an event listener for a button click:
HTML:
<button id="myButton">Click Me</button>

JavaScript:
function handleClick() {
    alert('Button clicked!');
}

document.getElementById('myButton').addEventListener('click', handleClick);
""",
        'example': """
            // Example 1:
            HTML:
            <button id="myButton">Click Me</button>

            JavaScript:
            function handleClick() {
                alert('Button clicked!');
            }

            document.getElementById('myButton').addEventListener('click', handleClick);
        """
    },
    {
        'name': 'removeEventListener',
        'trigger': 'remove event',
        'define': """'removeEventListener' is a method used to remove an event listener that was previously attached to an element with 'addEventListener()'. This method is essential for cleaning up event listeners to prevent memory leaks.

Syntax:
element.removeEventListener(event, listenerFunction);

Parameters:
- 'event' (required): A string that specifies the name of the event for which the listener was registered.
- 'listenerFunction' (required): The function that was previously attached as the event listener.

Example:
1. Removing an event listener for a button click:
HTML:
<button id="myButton">Click Me</button>

JavaScript:
function handleClick() {
    alert('Button clicked!');
}

let button = document.getElementById('myButton');
button.addEventListener('click', handleClick);

// After some time, remove the event listener
button.removeEventListener('click', handleClick);
""",
        'example': """
            // Example 1:
            HTML:
            <button id="myButton">Click Me</button>

            JavaScript:
            function handleClick() {
                alert('Button clicked!');
            }

            let button = document.getElementById('myButton');
            button.addEventListener('click', handleClick);

            // After some time, remove the event listener
            button.removeEventListener('click', handleClick);
        """
    },
    {
        'name': 'Propagation (Event Bubbling and Capturing)',
        'trigger': 'propagation',
        'define': """Event propagation refers to the way events are handled when an element's event triggers on nested elements. There are two main types of event propagation in the DOM: event bubbling and event capturing.

1. Event Bubbling:
   - When an event occurs on an element, it triggers the event on itself first, then on its parent element, and so on up to the root of the document.
   - Most events bubble by default, and you can use 'event.stopPropagation()' inside an event listener to stop the event from further propagating.

2. Event Capturing (or Event Trickling):
   - Event capturing is the opposite of event bubbling. The event is triggered on the root element first and then propagates down the DOM hierarchy to the target element.

Example:
1. Event Bubbling and Capturing:
HTML:
<div id="outer">
    <div id="inner">
        <button id="myButton">Click Me</button>
    </div>
</div>

JavaScript:
function handleClick(event) {
    console.log('Target:', event.target.id);
    console.log('Current Target:', event.currentTarget.id);
}

let button = document.getElementById('myButton');
let inner = document.getElementById('inner');
let outer = document.getElementById('outer');

button.addEventListener('click', handleClick);
inner.addEventListener('click', handleClick, true); // Use 'true' for event capturing
outer.addEventListener('click', handleClick, true);
""",
        'example': """
            // Example 1:
            HTML:
            <div id="outer">
                <div id="inner">
                    <button id="myButton">Click Me</button>
                </div>
            </div>

            JavaScript:
            function handleClick(event) {
                console.log('Target:', event.target.id);
                console.log('Current Target:', event.currentTarget.id);
            }

            let button = document.getElementById('myButton');
            let inner = document.getElementById('inner');
            let outer = document.getElementById('outer');

            button.addEventListener('click', handleClick);
            inner.addEventListener('click', handleClick, true); // Use 'true' for event capturing
            outer.addEventListener('click', handleClick, true);
        """
    },
    {
        'name': 'localStorage',
        'trigger': 'local storage',
        'define': """'localStorage' is a feature in modern web browsers that allows you to store key-value pairs locally in the user's browser. It provides a simple way to persistently store data, such as user preferences, settings, or small amounts of data, even when the user closes the browser or navigates away from the page.

Data stored in 'localStorage' is available across sessions, meaning the data will persist even after the browser is closed and reopened.

Example (Storing and retrieving data in 'localStorage'):
// Storing data in 'localStorage'
localStorage.setItem('username', 'JohnDoe');
localStorage.setItem('theme', 'dark');

// Retrieving data from 'localStorage'
let username = localStorage.getItem('username');
let theme = localStorage.getItem('theme');

console.log(username); // Output: 'JohnDoe'
console.log(theme);    // Output: 'dark'
""",
        'example': """
            // Example 1:
            // Storing data in 'localStorage'
            localStorage.setItem('username', 'JohnDoe');
            localStorage.setItem('theme', 'dark');

            // Retrieving data from 'localStorage'
            let username = localStorage.getItem('username');
            let theme = localStorage.getItem('theme');

            console.log(username); // Output: 'JohnDoe'
            console.log(theme);    // Output: 'dark'
        """
    },
    {
        'name': 'sessionStorage',
        'trigger': 'session storage',
        'define': """'sessionStorage' is similar to 'localStorage', but the data stored in 'sessionStorage' is only available within the current browser session. Once the user closes the browser or tab, the data is cleared, and it won't persist across sessions.

Example (Storing and retrieving data in 'sessionStorage'):
// Storing data in 'sessionStorage'
sessionStorage.setItem('city', 'New York');
sessionStorage.setItem('language', 'English');

// Retrieving data from 'sessionStorage'
let city = sessionStorage.getItem('city');
let language = sessionStorage.getItem('language');

console.log(city);     // Output: 'New York'
console.log(language); // Output: 'English'
""",
        'example': """
            // Example 1:
            // Storing data in 'sessionStorage'
            sessionStorage.setItem('city', 'New York');
            sessionStorage.setItem('language', 'English');

            // Retrieving data from 'sessionStorage'
            let city = sessionStorage.getItem('city');
            let language = sessionStorage.getItem('language');

            console.log(city);     // Output: 'New York'
            console.log(language); // Output: 'English'
        """
    },
    {
        'name': 'IndexedDB',
        'trigger': 'indexed db',
        'define': """'IndexedDB' is a low-level API for client-side storage of significant amounts of structured data. Unlike 'localStorage' and 'sessionStorage', which store data in a simple key-value format, IndexedDB allows you to store complex data structures, query data using indexes, and work with large datasets efficiently.

IndexedDB is commonly used in web applications that require offline support or need to store large amounts of data locally.

Example (Creating an IndexedDB database and adding data):
// Open a database (if it doesn't exist, it will be created)
let request = indexedDB.open('myDatabase', 1);

// Event listener for successful database creation or upgrade
request.onsuccess = function(event) {
    let db = event.target.result;

    // Create a transaction and access the object store
    let transaction = db.transaction(['customers'], 'readwrite');
    let objectStore = transaction.objectStore('customers');

    // Add data to the object store
    let customer = { id: 1, name: 'John Doe', email: 'john@example.com' };
    objectStore.add(customer);

    console.log('Data added to the object store.');
};

// Event listener for database error
request.onerror = function(event) {
    console.log('Error:', event.target.errorCode);
};
""",
        'example': """
            // Example 1:
            // Open a database (if it doesn't exist, it will be created)
            let request = indexedDB.open('myDatabase', 1);

            // Event listener for successful database creation or upgrade
            request.onsuccess = function(event) {
                let db = event.target.result;

                // Create a transaction and access the object store
                let transaction = db.transaction(['customers'], 'readwrite');
                let objectStore = transaction.objectStore('customers');

                // Add data to the object store
                let customer = { id: 1, name: 'John Doe', email: 'john@example.com' };
                objectStore.add(customer);

                console.log('Data added to the object store.');
            };

            // Event listener for database error
            request.onerror = function(event) {
                console.log('Error:', event.target.errorCode);
            };
        """
    },
    {
        'name': 'fetch',
        'define': """The Fetch API is a modern JavaScript API used to make asynchronous network requests. It provides a more flexible and powerful alternative to traditional XMLHttpRequest. The Fetch API uses Promises to handle the responses, making it easier to write asynchronous code and avoiding callback hell.

The basic usage of the Fetch API involves calling the global 'fetch' function with the URL of the resource you want to fetch. This function returns a Promise that resolves to the Response object representing the response to the request. You can then use methods like 'json()', 'text()', 'blob()', etc., on the Response object to extract the data from the response.

Keep in mind that the Fetch API only rejects the Promise on network errors, not HTTP errors like 404 or 500. You need to check the 'ok' property of the Response object to verify if the request was successful or not.""",
        'example': """
            "Basic GET request using Fetch API:"
            fetch('https://api.example.com/data')
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error(error));

            "POST request with headers using Fetch API:"
            fetch('https://api.example.com/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    key: 'value',
                })
            })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error(error));"
        """
    },
    {
        'name': 'function',
        'define': """In JavaScript, a function is a reusable block of code that performs a specific task or calculates a value. Functions allow you to divide your code into smaller, manageable pieces, promoting code reusability and maintainability.

There are several ways to define functions in JavaScript:
1. Function Declaration:
    function greet() {
        console.log('Hello, world!');
    }

2. Function Expression (Anonymous Function):
    const greet = function() {
        console.log('Hello, world!');
    };

3. Arrow Function (Introduced in ES6):
    const greet = () => {
        console.log('Hello, world!');
    };

Functions can take parameters (input values) and return a value using the 'return' keyword. If a function doesn't explicitly return a value, it will return 'undefined' by default.

Examples of functions with parameters and return values:
function addNumbers(a, b) {
    return a + b;
}
console.log(addNumbers(3, 5)); // Output: 8

function calculateCircleArea(radius) {
    return Math.PI * radius * radius;
}
console.log(calculateCircleArea(5)); // Output: 78.53981633974483
""",
        'example': """"""
    },
    {
        'name': 'generator',
        'define': """Generators are special functions in JavaScript that can be paused and resumed during execution. They use the 'yield' keyword to produce a sequence of values, which can be iterated. Generators provide an elegant way to create iterators and are particularly useful for handling asynchronous operations.

To define a generator function, you use an asterisk (*) after the 'function' keyword. When you call a generator function, it doesn't execute the code immediately; instead, it returns an iterator object.

Examples of generator functions:
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}
const gen = numberGenerator();
console.log(gen.next().value); // Output: 1
console.log(gen.next().value); // Output: 2
console.log(gen.next().value); // Output: 3

function* fibonacciGenerator() {
    let [prev, curr] = [0, 1];
    while (true) {
        yield curr;
        [prev, curr] = [curr, prev + curr];
    }
}
const fibGen = fibonacciGenerator();
console.log(fibGen.next().value); // Output: 1
console.log(fibGen.next().value); // Output: 1
console.log(fibGen.next().value); // Output: 2
""",
        'example': """"""
    },
    {
        'name': 'hoisting',
        'define': """Hoisting is a JavaScript behavior where variable declarations and function declarations are moved to the top of their containing scope during the compilation phase. However, only the declarations are hoisted, not the initializations.

Hoisting applies to both variables declared with 'var' and functions declared using the 'function' keyword. Variables declared with 'let', 'const', or 'class' are not hoisted.

Example of variable hoisting:
console.log(x); // Output: undefined
var x = 5;
console.log(x); // Output: 5

Example of function hoisting:
foo(); // Output: 'Hello'
function foo() {
    console.log('Hello');
}
""",
        'example': """"""
    },
    {
        'name': 'iife (immediately invoked function expression)',
        'trigger': 'immediately invoked',
        'define': """An IIFE (Immediately Invoked Function Expression) is a function in JavaScript that is executed immediately after its creation. It helps create a private scope and avoid polluting the global namespace.

The syntax of an IIFE involves wrapping the function in parentheses and then immediately invoking it using an additional pair of parentheses.

IIFE is commonly used to create modules, avoid variable hoisting issues, and isolate code from the global scope.

Examples of IIFE:
(function() {
    console.log('IIFE executed!');
})(); // Output: 'IIFE executed!'

(function(name) {
    console.log('Hello, ' + name + '!');
})('John'); // Output: 'Hello, John!'
""",
        'example': """"""
    },
    {
        'name': 'immutable',
        'define': """Immutable.js is a library for JavaScript that provides immutable data structures. It ensures that the data remains unchanged after creation, making it easier to manage application state and prevent unintended modifications.

Immutable.js offers several data structures like List, Map, Set, etc., that cannot be modified directly. Instead, methods such as 'push()', 'pop()', 'set()', etc., return new instances with the modified data.

Example of creating an immutable list:
const { List } = require('immutable');
const list = List([1, 2, 3]);

Example of modifying an immutable list:
const newList = list.push(4);
console.log(list.size); // Output: 3
console.log(newList.size); // Output: 4
""",
        'example': """"""
    },
    {
        'name': 'iteration',
        'define': """Iteration refers to the process of repeatedly executing a block of code for each element in a collection, such as an array or an object. It allows you to perform the same operation on each item in the collection.

In JavaScript, there are several ways to iterate over collections:
1. for Loop: The traditional 'for' loop is commonly used for iterating over arrays and performing actions on each element.

Example of using 'for' loop for array iteration:
const arr = [1, 2, 3];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

2. forEach() Method: The 'forEach()' method is available on arrays and provides a more concise way to iterate over array elements.

Example of using 'forEach()' method for array iteration:
arr.forEach(item => console.log(item));

3. for...of Loop: Introduced in ES6, the 'for...of' loop provides a convenient way to iterate over iterable objects, including arrays, strings, maps, sets, etc.

Example of using 'for...of' loop for array iteration:
for (const item of arr) {
    console.log(item);
}

4. for...in Loop: The 'for...in' loop is used to iterate over the properties of an object. However, it is not recommended for iterating over arrays due to potential issues with the iteration order and non-numeric keys.

Example of using 'for...in' loop for object iteration:
const obj = { name: 'John', age: 30 };
for (const key in obj) {
    console.log(key + ': ' + obj[key]);
}

It's important to choose the appropriate iteration method depending on the type of collection you are working with to ensure efficient and correct iteration of elements.
""",
        'example': """"""
    },
    {
        'name': 'jest',
        'define': """Jest is a popular JavaScript testing framework that is widely used for testing applications, particularly React applications. It provides a simple and efficient way to write unit tests and perform various testing tasks.

Jest is designed to be easy to set up and use. It comes with built-in support for mocking, assertions, and code coverage reporting. Jest runs tests in parallel, which helps to speed up the testing process.

Some key features of Jest include:
- Zero Configuration: Jest requires minimal setup and can run tests without the need for a separate configuration file, making it beginner-friendly.
- Mocking: Jest provides powerful mocking capabilities, allowing you to simulate the behavior of external dependencies and focus on testing individual units in isolation.
- Snapshot Testing: Snapshot testing allows you to capture the rendered output of components and compare it against the expected output, making it easier to detect unexpected changes.
- Asynchronous Testing: Jest simplifies testing asynchronous code using methods like 'async/await', 'Promise.resolve', and 'Promise.reject'.
- Code Coverage: Jest generates code coverage reports, enabling you to identify areas of code that are not adequately covered by tests.

Example of a basic test with Jest:
function add(a, b) {
    return a + b;
}
test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
});

Example of testing asynchronous code with Jest (using async/await):
function fetchData() {
    return new Promise(resolve => resolve('data'));
}
test('fetchData returns data', async () => {
    const data = await fetchData();
    expect(data).toBe('data');
});
""",
        'example': """"""
    },
    {
        'name': 'jquery',
        'define': """jQuery is a fast, small, and feature-rich JavaScript library. It simplifies HTML document traversal and manipulation, event handling, animation, and Ajax interactions.

jQuery allows you to write concise and efficient code to perform common tasks. It abstracts many of the complexities of JavaScript and provides a consistent and easy-to-use API.

Some key features of jQuery include:
- DOM Manipulation: jQuery provides a set of methods to select and manipulate HTML elements, making it easier to add, remove, or modify content on a web page.
- Event Handling: jQuery simplifies event handling by providing methods to attach event listeners to elements, such as 'click', 'mouseover', 'keyup', etc.
- Ajax: jQuery makes Ajax interactions more accessible with methods like '$.ajax()', '$.get()', and '$.post()', allowing you to load data from a server without a full page refresh.
- Animation: jQuery provides a wide range of animation effects, such as fading, sliding, and toggling elements, making it easier to create interactive and visually appealing web pages.
- Plugin Support: jQuery has a vibrant community that creates plugins, extending its functionality and providing solutions for various common tasks.

Example of basic DOM manipulation with jQuery:
<div id='myDiv'>Hello</div>
<script src='jquery.min.js'></script>
<script>
    // Change the content of the div
    $('#myDiv').text('Hello, world!');
</script>

Example of Ajax request with jQuery:
function fetchData() {
    $.ajax({
        url: 'https://api.example.com/data',
        success: function(data) {
            console.log(data);
        },
        error: function(error) {
            console.error(error);
        }
    });
}
fetchData();
""",
        'example': """"""
    },
    {
        'name': 'json',
        'define': """JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is widely used for data serialization and communication between web clients and servers.

JSON data consists of key-value pairs, where keys are strings enclosed in double quotes, and values can be strings, numbers, booleans, arrays, or other JSON objects. JSON does not support functions or undefined values.

Example of a JSON object:
{
    "name": "John Doe",
    "age": 30,
    "isEmployed": true,
    "hobbies": ["reading", "traveling", "photography"],
    "address": {
        "city": "New York",
        "zipCode": "10001"
    }
}

JSON.stringify(): The 'JSON.stringify()' method is used to convert a JavaScript object or value to a JSON string.

Example of using JSON.stringify():
const data = {
    name: 'John Doe',
    age: 30,
    isEmployed: true
};
const jsonString = JSON.stringify(data);
console.log(jsonString); // Output: '{"name":"John Doe","age":30,"isEmployed":true}'

JSON.parse(): The 'JSON.parse()' method is used to convert a JSON string back into a JavaScript object.

Example of using JSON.parse():
const jsonString = '{"name":"John Doe","age":30,"isEmployed":true}';
const data = JSON.parse(jsonString);
console.log(data.name); // Output: 'John Doe'
""",
        'example': """"""
    },
    {
        'name': 'let',
        'define': """'let' is a keyword introduced in ECMAScript 6 (ES6) for declaring block-scoped variables in JavaScript. Variables declared with 'let' are similar to 'var' but have some key differences:

1. Block Scope: Variables declared with 'let' have block scope, which means they are only accessible within the block (a pair of curly braces) where they are defined. This behavior prevents variable hoisting issues that can occur with 'var'.

Example of block-scoped 'let' variable:
if (true) {
    let x = 10;
}
console.log(x); // Error: 'x' is not defined

2. Hoisting: While 'let' variables are hoisted like 'var', they are not initialized until the point of declaration. This is known as the "temporal dead zone," and accessing the variable before its declaration results in a ReferenceError.

Example of temporal dead zone with 'let':
console.log(x); // Error: Cannot access 'x' before initialization
let x = 10;

3. Redeclaration: Unlike 'var', you cannot redeclare the same variable within the same block scope using 'let'. Attempting to do so will result in a SyntaxError.

Example of redeclaration error with 'let':
let x = 10;
let x = 20; // Error: Identifier 'x' has already been declared

4. Global Object Property: When using 'let' at the top level of a script (outside of any function or block), the variable is not added as a property of the global object (e.g., 'window' in browsers), unlike 'var'.

Example of global object property with 'var':
var y = 5;
console.log(window.y); // Output: 5

Example of no global object property with 'let':
let z = 8;
console.log(window.z); // Output: undefined
""",
        'example': """"""
    },
    {
        'name': 'lodash',
        'trigger': 'low dash',
        'define': """Lodash is a popular JavaScript utility library that provides a wide range of helper functions for working with arrays, objects, strings, functions, and more. It offers a consistent and efficient API, making it easier to perform common tasks and solve complex problems in a more functional and declarative style.

Lodash functions are carefully optimized for performance and are widely used in various JavaScript projects. By using Lodash, you can reduce the amount of custom code you need to write and avoid reinventing the wheel.

Some key features of Lodash include:
1. Collection Manipulation: Lodash provides functions for working with arrays and objects, such as 'map()', 'filter()', 'reduce()', 'find()', 'groupBy()', and many others.
2. String Manipulation: Lodash offers utilities for string operations, including 'trim()', 'startsWith()', 'endsWith()', 'camelCase()', 'kebabCase()', and more.
3. Functional Programming: Lodash includes functions that enable functional programming paradigms, like 'curry()', 'partial()', 'debounce()', 'throttle()', and 'memoize()'.
4. Chaining: Lodash supports method chaining, allowing you to perform multiple operations in a single expression for a more concise and readable code.

Example of using Lodash to work with arrays:
const _ = require('lodash');

const numbers = [1, 2, 3, 4, 5];

// Using Lodash to get the sum of squared even numbers
const sumOfSquaredEvenNumbers = _.chain(numbers)
    .filter(num => num % 2 === 0)
    .map(num => num * num)
    .sum()
    .value();

console.log(sumOfSquaredEvenNumbers); // Output: 20
""",
        'example': """"""
    },
    {
        'name': 'map',
        'define': """In JavaScript, 'map' is a higher-order function that is used to transform elements of an array into a new array based on a provided mapping function. The 'map' function does not modify the original array; instead, it creates a new array with the same length as the original, containing the results of applying the mapping function to each element.

Syntax of 'map':
array.map((currentValue, index, array) => {
    // Return the new value for the element
});

Parameters:
- 'currentValue' (required): The current element being processed in the array.
- 'index' (optional): The index of the current element in the array.
- 'array' (optional): The array being processed.

Return Value:
The 'map' function returns a new array containing the values returned by the mapping function for each element of the original array.

Example of using 'map' to transform an array:
let numbers = [1, 2, 3, 4, 5];

let squaredNumbers = numbers.map((num) => {
    return num * num;
});

console.log(squaredNumbers); // Output: [1, 4, 9, 16, 25]

In this example, 'map' is used to create a new array 'squaredNumbers' where each element is the square of the corresponding element in the 'numbers' array.

Using Arrow Function Shorthand:
Since 'map' often involves simple transformations, it is common to use the arrow function shorthand for concise code.

Example of using arrow function shorthand with 'map':
let numbers = [1, 2, 3, 4, 5];

let squaredNumbers = numbers.map(num => num * num);

console.log(squaredNumbers); // Output: [1, 4, 9, 16, 25]

Mapping Objects:
The 'map' function can also be used to transform objects into new objects by manipulating their properties.

Example of using 'map' to transform an array of objects:
let persons = [
    { name: 'John', age: 30 },
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 35 }
];

let greetings = persons.map((person) => {
    return 'Hello, ' + person.name + '!';
});

console.log(greetings);
// Output: ["Hello, John!", "Hello, Alice!", "Hello, Bob!"]

In this example, 'map' is used to create a new array 'greetings' where each element is a greeting message based on the 'name' property of each object in the 'persons' array.

Mapping Undefined or Sparse Elements:
If some elements of the original array are 'undefined', 'map' skips those elements during the transformation.

Example of mapping undefined elements:
let numbers = [1, 2, , 4, 5]; // The third element is undefined

let doubledNumbers = numbers.map((num) => {
    return num * 2;
});

console.log(doubledNumbers); // Output: [2, 4, NaN, 8, 10]

In this example, the third element (undefined) is skipped during the mapping, resulting in 'NaN' (Not a Number) in the 'doubledNumbers' array.

The 'map' function is a powerful tool for data manipulation and transformation in JavaScript, enabling developers to efficiently process arrays and create new arrays based on specific criteria or operations.""",
        'example': """
            // Example of using 'map' to transform an array
            let numbers = [1, 2, 3, 4, 5];

            let doubledNumbers = numbers.map((num) => {
                return num * 2;
            });

            console.log(doubledNumbers); // Output: [2, 4, 6, 8, 10]
        """
    },
    {
        'name': 'mocha',
        'define': """Mocha is a feature-rich JavaScript testing framework for running both synchronous and asynchronous tests. It is often used for testing Node.js applications and server-side code. Mocha provides an easy-to-read and flexible testing syntax, making it popular among developers for writing unit tests, integration tests, and more.

Key features of Mocha include:
1. Test Suite: Mocha allows you to organize tests into test suites using the 'describe()' function, which makes test results more structured and easier to understand.
2. Test Cases: Each individual test is represented as a test case, created using the 'it()' function. You can use assertions inside test cases to validate expected outcomes.
3. Asynchronous Testing: Mocha supports asynchronous testing using callback functions, Promises, or 'async/await' syntax, making it easy to handle asynchronous operations during testing.
4. Hooks: Mocha provides hooks like 'before()', 'after()', 'beforeEach()', and 'afterEach()', which allow you to run setup and cleanup code before and after test cases or test suites.
5. Support for Various Reporters: Mocha supports different reporters to display test results in various formats, including the built-in 'spec' reporter, 'nyan' reporter, 'dot' reporter, and more.
6. Integration with Other Libraries: Mocha integrates well with assertion libraries like 'Chai', allowing you to choose the assertion style that suits your preferences.

Example of a basic Mocha test:
const assert = require('assert');

function add(a, b) {
    return a + b;
}

describe('add() function', () => {
    it('should return the sum of two numbers', () => {
        const result = add(2, 3);
        assert.strictEqual(result, 5);
    });
});
""",
        'example': """"""
    },
    {
        'name': 'module',
        'define': """In JavaScript, a module refers to a self-contained unit of code that can be exported, imported, and reused in other parts of the application. Modules help organize code and promote code encapsulation and reusability.

Prior to ES6 (ECMAScript 2015), JavaScript did not have native support for modules. Developers relied on various module patterns like the Revealing Module Pattern and CommonJS to achieve modularity.

With the introduction of ES6 modules, JavaScript officially supports a standardized way to create, import, and export modules. ES6 modules use the 'export' and 'import' keywords to control what gets exposed from a module and what gets imported into another module.

Example of exporting and importing modules in ES6:
// math.js (module)
export function add(a, b) {
    return a + b;
}

// app.js (module)
import { add } from './math.js';

console.log(add(2, 3)); // Output: 5

In Node.js, modules are also an essential part of the ecosystem, and CommonJS is the standard module format used. Node.js modules use 'module.exports' and 'require()' to export and import modules, respectively.

Example of exporting and importing modules in Node.js:
// math.js (module)
function add(a, b) {
    return a + b;
}
module.exports = { add };

// app.js (module)
const { add } = require('./math.js');

console.log(add(2, 3)); // Output: 5

Using modules, developers can break down complex applications into smaller, manageable pieces, making it easier to maintain and collaborate with other team members.
""",
        'example': """"""
    },
    {
        'name': 'nan',
        'define': """NaN (Not-a-Number) is a special value in JavaScript that represents an unrepresentable or undefined numerical result. It is returned when a mathematical operation or function fails to produce a meaningful numeric result.

NaN is a property of the global object and can be accessed using 'window.NaN' in browsers or 'global.NaN' in Node.js.

Examples of operations that result in NaN:
console.log(0 / 0); // Output: NaN
console.log(Math.sqrt(-1)); // Output: NaN

NaN is unique because it does not equal anything, including itself. To test if a value is NaN, you need to use the 'isNaN()' function or the global 'Number.isNaN()' method introduced in ES6.

Examples of checking for NaN:
console.log(isNaN(NaN)); // Output: true
console.log(Number.isNaN(NaN)); // Output: true

Note that 'isNaN()' returns true for any non-numeric value, so it's recommended to use 'Number.isNaN()' when specifically checking for NaN.
""",
        'example': """"""
    },
    {
        'name': 'node',
        'define': """Node.js is a server-side JavaScript runtime that allows developers to run JavaScript code outside of a web browser. It uses the V8 JavaScript engine, the same engine that powers Google Chrome, to execute JavaScript code on the server.

Node.js is designed to be fast, scalable, and efficient, making it well-suited for building real-time applications, APIs, server-side applications, and more.

Key features of Node.js include:
1. Asynchronous, Non-Blocking I/O: Node.js uses an event-driven, non-blocking I/O model, allowing it to handle multiple concurrent operations efficiently without blocking the execution of other code. This makes it ideal for handling high volumes of concurrent requests.
2. Built-in Modules: Node.js provides a set of core modules that enable various functionalities, such as 'http' for creating web servers, 'fs' for file system operations, 'path' for handling file paths, and more.
3. npm (Node Package Manager): npm is the default package manager for Node.js, and it is the largest ecosystem of open-source libraries and modules. Developers can easily install and manage third-party packages for their projects using npm.
4. Cross-Platform: Node.js is cross-platform, which means it can run on various operating systems, including Windows, macOS, and Linux.
5. Single-Threaded Event Loop: Node.js operates on a single-threaded event loop, but it can leverage the underlying operating system's multi-threaded capabilities to handle I/O operations efficiently.
6. Expressive Syntax: Node.js has a simple and expressive syntax that makes it easy to write server-side code using JavaScript, making it accessible to front-end developers familiar with the language.

Example of creating a basic HTTP server with Node.js:
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, Node.js!');
});

server.listen(3000, () => {
    console.log('Server is running at http://localhost:3000/');
});
""",
        'example': """"""
    },
    {
        'name': 'npm',
        'define': """npm (Node Package Manager) is the default package manager for Node.js, and it is the largest package registry for JavaScript libraries and modules. It allows developers to easily discover, install, and manage third-party packages for their Node.js projects.

npm operates through the command-line interface (CLI) and provides a vast ecosystem of open-source packages that can be easily integrated into projects. It also enables developers to publish and share their own packages with the community.

Key features of npm include:
1. Installation: npm provides a straightforward way to install packages from the npm registry into your project. It reads the dependencies specified in the 'package.json' file and installs them in the 'node_modules' directory.

Example of installing a package using npm:
npm install packageName

2. package.json: The 'package.json' file is a crucial part of any Node.js project. It contains metadata about the project, including its name, version, dependencies, scripts, and more. Developers can use the 'npm init' command to create a new 'package.json' file or modify an existing one.

3. Semantic Versioning: npm follows semantic versioning, where package versions consist of three numbers: 'MAJOR.MINOR.PATCH'. This allows developers to define version ranges for dependencies, ensuring compatibility and stability.

Example of specifying a package version in 'package.json':
"dependencies": {
    "packageName": "^1.2.0"
}

4. Scripts: The 'package.json' file also contains a 'scripts' section, allowing developers to define custom commands to be executed using 'npm run <scriptName>'.

Example of defining a script in 'package.json':
"scripts": {
    "start": "node app.js"
}

5. Publishing: Developers can publish their own packages to the npm registry, making them available for other developers to use. The 'npm publish' command is used to publish packages.

Example of publishing a package to npm:
npm publish

6. Version Management: npm provides commands to update packages to their latest versions, check for outdated dependencies, and manage version conflicts.

Example of checking for outdated packages:
npm outdated

npm plays a crucial role in the Node.js ecosystem and facilitates the sharing and collaboration of code among developers worldwide.
""",
        'example': """"""
    },
    {
        'name': 'null',
        'define': """In JavaScript, 'null' is a special value that represents the absence of any value or an empty reference. It is a primitive data type and typically used to indicate that a variable or object property has no value or has not been assigned a value yet.

Example of assigning a variable to null:
let value = null;

The typeof 'null' is 'object', which is a historical mistake and not a precise representation of its nature. To check if a variable is 'null', you can use the '===' or '!===' strict equality operators.

Example of checking for null:
let value = null;
if (value === null) {
    console.log('The value is null.');
}

It's essential to distinguish between 'null' and 'undefined'. 'null' is a value that can be explicitly assigned, while 'undefined' typically represents an uninitialized variable or an object property that does not exist.

Example of 'undefined':
let name;
console.log(name); // Output: undefined

When working with APIs or data sources, 'null' is commonly used to represent the absence of data or a valid response.
""",
        'example': """"""
    },
    {
        'name': 'object',
        'define': """In JavaScript, an object is a composite data type that allows you to store collections of key-value pairs. Objects are fundamental to JavaScript and play a central role in the language.

Objects can be created using either the object literal notation (curly braces) or the 'Object' constructor.

Example of creating an object using object literal notation:
const person = {
    name: 'John Doe',
    age: 30,
    isEmployed: true
};

Example of creating an object using the 'Object' constructor:
const person = new Object();
person.name = 'John Doe';
person.age = 30;
person.isEmployed = true;

Objects in JavaScript are dynamic, which means you can add, modify, or delete properties at any time.

Accessing Object Properties:
You can access the properties of an object using dot notation or square brackets notation.

Example of accessing object properties:
const person = {
    name: 'John Doe',
    age: 30,
    isEmployed: true
};

console.log(person.name); // Output: 'John Doe'
console.log(person['age']); // Output: 30

Iterating Over Object Properties:
To loop through the properties of an object, you can use a 'for...in' loop or methods like 'Object.keys()', 'Object.values()', or 'Object.entries()' introduced in ES6.

Example of iterating over object properties with 'for...in' loop:
const person = {
    name: 'John Doe',
    age: 30,
    isEmployed: true
};

for (const key in person) {
    console.log(key + ': ' + person[key]);
}

Objects are widely used in JavaScript for representing data structures, configurations, and complex entities in applications.
""",
        'example': """"""
    },
    {
        'name': 'promise',
        'define': """A promise is an object in JavaScript used for handling asynchronous operations. It represents a value that may not be available yet but will be resolved (fulfilled) or rejected in the future, typically after an asynchronous operation completes.

Promises provide a cleaner and more readable way to deal with asynchronous code compared to traditional callbacks, known as "callback hell."

Creating a Promise:
A Promise is created using the 'Promise' constructor, which takes a callback function with two arguments: 'resolve' and 'reject'. Inside the callback, you perform the asynchronous operation and call 'resolve()' when the operation is successful or 'reject()' when it encounters an error.

Example of creating a simple Promise:
const promise = new Promise((resolve, reject) => {
    // Simulating an asynchronous operation
    setTimeout(() => {
        const data = 'Async operation completed successfully!';
        resolve(data); // The promise is fulfilled with the data
    }, 2000);
});

Handling Promise Results:
To handle the result of a Promise, you use the 'then()' method. It takes two callback functions as arguments: the first for the fulfilled (successful) case and the second for the rejected (error) case.

Example of handling the result of a Promise:
promise.then(
    (data) => {
        console.log(data); // Output: 'Async operation completed successfully!'
    },
    (error) => {
        console.error(error);
    }
);

Chaining Promises:
Promises can be chained together using the 'then()' method. This is useful for sequential asynchronous operations or transforming the data between steps.

Example of chaining Promises:
function fetchData() {
    return new Promise((resolve, reject) => {
        // Simulating an asynchronous operation
        setTimeout(() => {
            const data = 'Async operation completed successfully!';
            resolve(data);
        }, 2000);
    });
}

fetchData()
    .then((data) => {
        console.log(data); // Output: 'Async operation completed successfully!'
        return data.toUpperCase();
    })
    .then((upperCaseData) => {
        console.log(upperCaseData); // Output: 'ASYNC OPERATION COMPLETED SUCCESSFULLY!'
    })
    .catch((error) => {
        console.error(error);
    });

The 'catch()' method is used to handle errors in the Promise chain. It will catch any rejected promises in the chain.

Async/Await:
ES8 introduced async/await, which provides a more synchronous-looking syntax for handling promises. The 'async' keyword is used to define an asynchronous function, and 'await' is used to wait for the promise to resolve or reject.

Example of using async/await:
async function fetchData() {
    return new Promise((resolve, reject) => {
        // Simulating an asynchronous operation
        setTimeout(() => {
            const data = 'Async operation completed successfully!';
            resolve(data);
        }, 2000);
    });
}

async function processAsyncData() {
    try {
        const data = await fetchData();
        console.log(data); // Output: 'Async operation completed successfully!'
    } catch (error) {
        console.error(error);
    }
}

processAsyncData();
""",
        'example': """"""
    },
    {
        'name': 'prototype',
        'define': """In JavaScript, every object is associated with a prototype object, which acts as a blueprint for that object. The prototype contains properties and methods that are inherited by all instances of that object type.

Prototypes form the basis of JavaScript's prototypal inheritance model. When you access a property or method on an object, and it is not found on the object itself, JavaScript will look for it in the object's prototype chain.

Creating Objects with Prototypes:
In JavaScript, you can create objects and link them to prototypes using either constructor functions or the modern class syntax introduced in ES6.

Example using constructor function:
function Person(name) {
    this.name = name;
}
Person.prototype.sayHello = function() {
    console.log('Hello, my name is ' + this.name);
};

const john = new Person('John');
john.sayHello(); // Output: 'Hello, my name is John'

In the example above, 'Person.prototype' becomes the prototype of all instances created with the 'Person' constructor. Any object created with 'new Person()' will have access to the 'sayHello' method through the prototype chain.

Class syntax (ES6 and beyond):
class Person {
    constructor(name) {
        this.name = name;
    }

    sayHello() {
        console.log('Hello, my name is ' + this.name);
    }
}

const john = new Person('John');
john.sayHello(); // Output: 'Hello, my name is John'

Object.prototype:
The 'Object.prototype' is the ultimate prototype in JavaScript. It is the topmost object in the prototype chain and includes methods and properties inherited by all objects.

Example of a common method from 'Object.prototype':
const person = {
    name: 'John',
    age: 30
};

console.log(Object.keys(person)); // Output: ['name', 'age']

In the example above, 'Object.keys()' is used to retrieve an array of the object's own enumerable property names. The 'Object.keys()' method is available to all objects in JavaScript since all objects inherit from 'Object.prototype'.

It's important to be cautious when modifying the 'Object.prototype' or adding properties directly to it, as this can lead to unexpected behavior and compatibility issues with other code.
""",
        'example': """"""
    },
    
    {
        'name': 'react',
        'define': """React is a popular JavaScript library for building user interfaces. It was developed and is maintained by Facebook. React allows developers to create reusable UI components and efficiently manage the state of an application, making it an essential tool for building interactive and dynamic web applications.

Key features of React include:
1. Component-Based Architecture: React follows a component-based architecture, where UIs are divided into smaller, reusable components. This encourages code reusability and maintainability.
2. Virtual DOM: React uses a virtual representation of the actual DOM, called the Virtual DOM, to optimize rendering. When the state of a component changes, React efficiently updates only the necessary parts of the actual DOM, reducing the number of expensive DOM operations.
3. JSX (JavaScript XML): React uses JSX, which is a syntax extension for JavaScript. JSX allows developers to write HTML-like code directly in JavaScript, making it easier to describe the structure of the UI.
4. Unidirectional Data Flow: React follows a unidirectional data flow, meaning data flows only in one direction, from parent components to child components. This makes the application more predictable and easier to debug.
5. React Hooks: Introduced in React 16.8, hooks are functions that allow developers to use state and other React features in functional components, eliminating the need for class components in many cases.
6. React Router: React Router is a library that provides routing capabilities to React applications, enabling developers to build single-page applications with multiple views.
7. Context API: React's Context API allows developers to pass data through the component tree without the need to pass props down explicitly at each level.
8. React Native: React can be used to build native mobile applications through React Native, a framework that allows developers to write mobile apps using JavaScript and React components. React Native provides a bridge between JavaScript and the native components of the target platform.

Example of a simple React component using JSX:
import React from 'react';

const Greeting = () => {
    return <h1>Hello, React!</h1>;
};

9. Reusable Components: React promotes reusability, and developers can create their own custom components and use them throughout the application.

Example of a reusable custom component:
import React from 'react';

const Button = ({ onClick, children }) => {
    return <button onClick={onClick}>{children}</button>;
};

10. Developer Tools: React has excellent developer tools that help with debugging, inspecting components, and monitoring performance.

React has a thriving ecosystem, with a vast number of third-party libraries and extensions available through npm. Its flexibility, performance optimizations, and ease of development have made it a popular choice for frontend development.
""",
        'example': """"""
    },
    {
        'name': 'recursion',
        'define': """Recursion is a programming technique where a function calls itself to solve a problem. Instead of using iterative loops, recursion allows developers to break down complex problems into smaller, more manageable subproblems.

In recursion, there are two main components:
1. Base Case: The base case is the condition that terminates the recursion. It provides a stopping point to prevent infinite recursion and defines the simplest version of the problem that can be directly solved without further recursion.
2. Recursive Case: The recursive case is where the function calls itself with a modified version of the problem to move towards the base case. Each recursive call solves a smaller part of the problem until the base case is reached.

Example of a simple recursive function to calculate factorial:
function factorial(n) {
    if (n === 0 || n === 1) {
        return 1; // Base case
    } else {
        return n * factorial(n - 1); // Recursive case
    }
}

console.log(factorial(5)); // Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)

Recursion can be a powerful technique for solving problems that have a repetitive or self-similar structure. However, it's essential to ensure that there is a proper base case and that the recursion does not result in infinite loops.

Tail Recursion:
Tail recursion is a specific form of recursion where the recursive call is the last operation performed in the function before returning a value. Some programming languages and compilers can optimize tail-recursive functions to avoid stack overflow errors.

Example of a tail-recursive function for calculating factorial:
function factorial(n, acc = 1) {
    if (n === 0) {
        return acc;
    } else {
        return factorial(n - 1, acc * n);
    }
}

console.log(factorial(5)); // Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)

While recursion can be an elegant solution for certain problems, it may not always be the most efficient approach. In some cases, iterative solutions or other algorithms may offer better performance and readability.
""",
        'example': """"""
    },
     {
        'name': 'redux',
        'define': """Redux is a state management library for JavaScript applications, particularly those built with frameworks like React. It provides a predictable state container that helps manage the state of an application in a consistent and organized way.

Key concepts of Redux include:
1. Store: The store is a single source of truth for the entire application state. It holds the complete state tree and allows access to the state using a 'getState()' method. The state in the Redux store is read-only, and the only way to change it is by dispatching actions.

2. Actions: Actions are plain JavaScript objects that represent the intention to change the state. They are dispatched to the Redux store using the 'dispatch()' method. Actions must have a 'type' property that describes the type of action being performed.

Example of a Redux action:
const incrementCounter = {
    type: 'INCREMENT',
};

3. Reducers: Reducers are pure functions that take the current state and an action as arguments and return a new state based on the action type. Reducers define how the application's state changes in response to actions. They should not modify the original state but create a new copy with the desired changes.

Example of a simple Redux reducer:
const counterReducer = (state = 0, action) => {
    switch (action.type) {
        case 'INCREMENT':
            return state + 1;
        default:
            return state;
    }
};

4. Dispatching Actions: To modify the state in the Redux store, you dispatch actions using the 'dispatch()' method. The store then calls the appropriate reducer, updates the state, and notifies all subscribed components of the state change.

Example of dispatching an action in a React component:
import { useDispatch } from 'react-redux';
import { incrementCounter } from './actions';

const CounterComponent = () => {
    const dispatch = useDispatch();

    const handleIncrement = () => {
        dispatch(incrementCounter());
    };

    return (
        <div>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    );
};

5. Middleware: Redux allows the use of middleware, which are functions that intercept dispatched actions before they reach the reducers. Middleware can be used for various purposes, such as logging actions, making asynchronous calls, or modifying actions before they reach the reducers.

Example of using Redux middleware (thunk) for making an asynchronous API call:
import { useDispatch } from 'react-redux';
import { fetchData } from './actions';

const DataComponent = () => {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchData()); // Dispatch an action to fetch data asynchronously
    }, []);

    // ...
};

6. React-Redux: React-Redux is a library that provides integration between React and Redux. It allows React components to interact with the Redux store, dispatch actions, and subscribe to changes in the store.

Example of connecting a React component to the Redux store:
import { useSelector, useDispatch } from 'react-redux';
import { incrementCounter } from './actions';

const CounterComponent = () => {
    const count = useSelector(state => state.counter);
    const dispatch = useDispatch();

    const handleIncrement = () => {
        dispatch(incrementCounter());
    };

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    );
};

Redux provides a well-defined pattern for managing application state, making it easier to reason about complex state changes and ensuring that the state remains predictable and consistent across the entire application.
""",
        'example': """"""
    },
    {
        'name': 'regexp',
        'define': """A regular expression, often abbreviated as regexp or regex, is a powerful pattern-matching tool used in JavaScript and many other programming languages. It allows developers to search, match, and manipulate text based on patterns.

In JavaScript, regular expressions are represented by objects of the 'RegExp' class or by using a regex literal notation, which is enclosed in forward slashes ('/').

Example of a regular expression to match all occurrences of the word 'hello' in a text:
const text = 'Hello, hello, and hello again!';
const regex = /hello/g; // 'g' flag for global search

const matches = text.match(regex);
console.log(matches); // Output: ['hello', 'hello', 'hello']

Common Flags for Regular Expressions:
1. 'g' (Global): When this flag is used, the regular expression searches for all occurrences of the pattern, not just the first one.

2. 'i' (Case-Insensitive): With this flag, the regular expression ignores the case while matching, so 'A' will match 'a', and vice versa.

3. 'm' (Multiline): When enabled, the '^' and '$' anchors match the start and end of each line instead of the whole string.

Example of using flags:
const text = 'Hello, hello, and hello again!';
const regex = /hello/gi; // 'g' and 'i' flags

const matches = text.match(regex);
console.log(matches); // Output: ['Hello', 'hello', 'hello']

Common Methods for Regular Expressions:
1. 'test()': The 'test()' method checks if the pattern matches any part of the given string and returns a boolean.

Example of using 'test()':
const text = 'Hello, World!';
const regex = /hello/i;

const isMatch = regex.test(text);
console.log(isMatch); // Output: true

2. 'match()': The 'match()' method returns an array containing all matches of the pattern in the given string. If the 'g' flag is used, it returns all matches; otherwise, it returns only the first match and additional information.

3. 'exec()': The 'exec()' method returns an array containing details about the first match or null if no match is found. If the 'g' flag is used, it returns successive matches on each call.

Example of using 'exec()':
const text = 'Hello, World!';
const regex = /hello/i;

let result;
while ((result = regex.exec(text)) !== null) {
    console.log('Found match:', result[0]);
}

Regular expressions are extremely versatile and can be used for tasks like validation, text search and replace, extracting data from strings, and more. However, they can also be complex and challenging to read and write, especially for beginners.
""",
        'example': """"""
    },
    {
        'name': 'scope',
        'define': """Scope in JavaScript refers to the context in which variables and functions are accessible. It determines the visibility and lifetime of variables and defines where a particular value can be accessed or modified within a program.

In JavaScript, there are two main types of scope:
1. Global Scope: Variables declared outside any function or block have global scope and can be accessed from anywhere within the script. Global variables are attached to the global object ('window' in browsers, 'global' in Node.js).

Example of a global variable:
const globalVar = 'I am global!';

function exampleFunction() {
    console.log(globalVar); // Output: 'I am global!'
}

2. Local Scope: Variables declared within a function or block have local scope and are accessible only within that specific function or block. Local variables are not visible outside the function or block where they are defined.

Example of a local variable:
function exampleFunction() {
    const localVar = 'I am local!';
    console.log(localVar); // Output: 'I am local!'
}

console.log(localVar); // Error: 'localVar' is not defined

Shadowing:
When a variable in a local scope has the same name as a variable in a higher-level scope, it is said to "shadow" the outer variable. The inner variable takes precedence over the outer variable within its scope.

Example of variable shadowing:
const message = 'Hello, global!';

function exampleFunction() {
    const message = 'Hi, local!';
    console.log(message); // Output: 'Hi, local!'
}

exampleFunction();
console.log(message); // Output: 'Hello, global!'

Block Scope:
Prior to ES6 (ECMAScript 2015), JavaScript had function scope, which meant variables were only scoped to the function in which they were declared. However, ES6 introduced block scope with the 'let' and 'const' keywords.

Example of block scope using 'let':
function exampleFunction() {
    if (true) {
        let blockVar = 'I am block-scoped!';
        console.log(blockVar); // Output: 'I am block-scoped!'
    }
    console.log(blockVar); // Error: 'blockVar' is not defined
}

Lexical Scope (Closures):
Lexical scope, also known as closures, is a concept where a function can access variables from its containing (outer) scope, even after the outer function has finished executing.

Example of a closure:
function outerFunction() {
    const outerVar = 'I am outer!';

    function innerFunction() {
        console.log(outerVar); // Output: 'I am outer!'
    }

    return innerFunction;
}

const closureFunc = outerFunction();
closureFunc();

In the example above, 'innerFunction' forms a closure over 'outerVar', allowing it to access the variable even after 'outerFunction' has finished executing.

Understanding scope is essential for managing variable names, avoiding naming conflicts, and optimizing memory usage in JavaScript programs.
""",
        'example': """"""
    },
    {
        'name': 'set',
        'define': """In JavaScript, 'Set' is a built-in data structure that represents an ordered collection of unique values. Unlike arrays, 'Set' does not allow duplicate elements, which means every value in a 'Set' must be unique.

Creating a Set:
You can create a new 'Set' by passing an iterable (such as an array) to the 'Set' constructor.

Example of creating a Set:
const mySet = new Set([1, 2, 3, 3, 4, 5]);

console.log(mySet); // Output: Set { 1, 2, 3, 4, 5 }

Set Methods:
Sets have various methods to manipulate and retrieve elements.

1. 'add(value)': Adds a new element to the Set. If the value already exists, it will not be added again.

Example of using 'add()':
const mySet = new Set();
mySet.add(1);
mySet.add(2);
mySet.add(3);
mySet.add(3); // Duplicate value, will be ignored

console.log(mySet); // Output: Set { 1, 2, 3 }

2. 'delete(value)': Removes the specified value from the Set.

Example of using 'delete()':
const mySet = new Set([1, 2, 3]);
mySet.delete(2);

console.log(mySet); // Output: Set { 1, 3 }

3. 'has(value)': Checks if the specified value is present in the Set and returns a boolean.

Example of using 'has()':
const mySet = new Set([1, 2, 3]);
console.log(mySet.has(2)); // Output: true
console.log(mySet.has(4)); // Output: false

4. 'size': Returns the number of elements in the Set.

Example of using 'size':
const mySet = new Set([1, 2, 3]);
console.log(mySet.size); // Output: 3

5. 'clear()': Removes all elements from the Set, making it empty.

Example of using 'clear()':
const mySet = new Set([1, 2, 3]);
mySet.clear();

console.log(mySet); // Output: Set {}

Iterating through a Set:
Sets can be iterated using loops or the 'forEach()' method.

Example of iterating through a Set using a loop:
const mySet = new Set([1, 2, 3]);

for (const value of mySet) {
    console.log(value);
}
// Output:
// 1
// 2
// 3

Example of iterating through a Set using 'forEach()':
const mySet = new Set([1, 2, 3]);

mySet.forEach((value) => {
    console.log(value);
});
// Output:
// 1
// 2
// 3

Converting Set to Array:
To convert a Set to an array, you can use the 'Array.from()' method or the spread operator.

Example of converting a Set to an array using 'Array.from()':
const mySet = new Set([1, 2, 3]);
const myArray = Array.from(mySet);

console.log(myArray); // Output: [1, 2, 3]

Example of converting a Set to an array using the spread operator:
const mySet = new Set([1, 2, 3]);
const myArray = [...mySet];

console.log(myArray); // Output: [1, 2, 3]

Sets are useful when you need to ensure uniqueness and don't require the elements to be indexed, as in the case of arrays.
""",
        'example': """"""
    },
    {
        'name': 'setTimeout',
        'trigger': 'set timeout',
        'define': """'setTimeout' is a built-in function in JavaScript used to schedule the execution of a function (or an expression) after a specified delay in milliseconds. It allows you to introduce time-based operations in JavaScript, such as delaying the execution of a piece of code or implementing animations.

Syntax of 'setTimeout':
The basic syntax of 'setTimeout' is as follows:
setTimeout(callbackFunction, delayInMilliseconds, arg1, arg2, ...);

Parameters:
- 'callbackFunction': The function to be executed after the specified delay.
- 'delayInMilliseconds': The time delay in milliseconds before executing the function.
- 'arg1', 'arg2', ...: Optional arguments that can be passed to the callbackFunction.

Example of using 'setTimeout':
function delayedGreeting(name) {
    console.log('Hello, ' + name + '!');
}

setTimeout(delayedGreeting, 2000, 'John');
// After 2 seconds, the function 'delayedGreeting' will be called with the argument 'John'
// Output after 2 seconds: 'Hello, John!'

Clearing a Timeout:
You can cancel a scheduled timeout using the 'clearTimeout()' method. This prevents the callback function from being executed if the timeout has not already occurred.

Syntax of 'clearTimeout':
const timeoutID = setTimeout(callbackFunction, delayInMilliseconds);
clearTimeout(timeoutID);

Example of clearing a timeout:
function delayedGreeting(name) {
    console.log('Hello, ' + name + '!');
}

const timeoutID = setTimeout(delayedGreeting, 2000, 'John');
clearTimeout(timeoutID); // The timeout is cleared, and 'delayedGreeting' will not be executed

Repeating a Function with 'setInterval':
The 'setInterval' function is similar to 'setTimeout', but instead of executing the callback function once after the delay, it repeatedly executes the callback at a specified interval until cleared.

Syntax of 'setInterval':
const intervalID = setInterval(callbackFunction, intervalInMilliseconds, arg1, arg2, ...);

Parameters:
- 'callbackFunction': The function to be repeatedly executed.
- 'intervalInMilliseconds': The time interval in milliseconds between each execution.
- 'arg1', 'arg2', ...: Optional arguments that can be passed to the callbackFunction.

Example of using 'setInterval':
function printTime() {
    console.log(new Date().toLocaleTimeString());
}

const intervalID = setInterval(printTime, 1000);
// Output every second: the current time in the local time zone

To stop the repeated execution, you can use 'clearInterval(intervalID)'.

Using 'setTimeout' and 'setInterval' is essential for handling time-dependent operations in JavaScript, such as animations, delayed actions, or periodic updates.
""",
        'example': """"""
    },
    {
        'name': 'strict mode',
        'trigger': 'strict mode',
        'define': """Strict mode is a feature introduced in ECMAScript 5 (ES5) to make JavaScript code more robust by enforcing stricter rules and eliminating certain unsafe and problematic language features. When strict mode is enabled, the JavaScript runtime will report errors for common coding mistakes, which helps developers write more reliable and maintainable code.

Enabling Strict Mode:
Strict mode is enabled by adding the following string literal at the beginning of a script or function:
'use strict';

Global Strict Mode:
In a global context (outside any function), enabling strict mode affects the entire script.

Example of enabling strict mode in a script:
'use strict';

// Now, the entire script is in strict mode
// Any mistakes or unsafe practices will throw errors

Function Strict Mode:
In a function scope, enabling strict mode affects only that specific function and its inner functions.

Example of enabling strict mode in a function:
function myFunction() {
    'use strict';

    // Only this function and its inner functions are in strict mode
}

Strict Mode Rules and Benefits:
1. Prevents Undeclared Variables: In non-strict mode, assigning a value to an undeclared variable creates a global variable. In strict mode, this behavior is disallowed, and assigning to an undeclared variable will result in a reference error.

2. Eliminates Octal Literal Syntax: Octal number syntax, like '012', is not allowed in strict mode, as it can be confusing and error-prone.

3. Disallows Duplicate Function Parameters: Strict mode prevents the use of duplicate parameter names in function declarations or expressions.

4. Prohibits 'with' Statement: The 'with' statement, which can lead to unpredictable behavior and performance issues, is not allowed in strict mode.

5. Prevents Overwriting of Properties in Objects: In non-strict mode, it is possible to accidentally overwrite non-writable properties of an object silently. In strict mode, such assignments will throw a type error.

6. Requires 'eval' and 'arguments' to Be Treated as Keywords: In strict mode, 'eval' and 'arguments' are reserved keywords, meaning they cannot be used as variable names.

7. Eliminates 'delete' on Non-Configurable Properties: In strict mode, 'delete' cannot be used to remove properties that are marked as non-configurable.

Example of a strict mode violation:
'use strict';
x = 10; // Error: 'x' is not defined

Advantages of Strict Mode:
- Helps catch errors and potential bugs early in development.
- Encourages better coding practices and avoids common pitfalls.
- Makes the code easier to optimize by the JavaScript engine, leading to potential performance improvements.

Note: It's recommended to use strict mode in all JavaScript code to ensure better code quality and maintainability.
""",
        'example': """"""
    },
    {
        'name': 'string',
        'define': """In JavaScript, a 'string' is a data type that represents a sequence of characters. Strings are used to store and manipulate text-based data, such as names, sentences, or any other textual information.

Creating Strings:
Strings can be created in JavaScript using single quotes (''), double quotes (""), or backticks (``). Backticks, introduced in ECMAScript 6 (ES6), are used for template literals, which offer advanced string interpolation features.

Examples of creating strings:
const singleQuotesString = 'Hello, I am a string.';
const doubleQuotesString = "I am also a string.";
const templateLiteralString = `I am a template literal string.`;

Special Characters in Strings:
Strings can contain special escape sequences to represent characters that cannot be typed directly, such as newlines, tabs, or quotation marks.

Examples of special escape sequences:
const newLineString = "First line\nSecond line";
const tabString = "Name:\tJohn";
const quoteString = "He said, \"Hello!\"";

String Length:
To get the length of a string (the number of characters), you can use the 'length' property of the string object.

Example of getting the length of a string:
const myString = "Hello, World!";
console.log(myString.length); // Output: 13

String Concatenation:
You can concatenate (combine) strings using the '+' operator.

Example of string concatenation:
const firstName = "John";
const lastName = "Doe";
const fullName = firstName + " " + lastName;
console.log(fullName); // Output: "John Doe"

String Methods:
JavaScript provides several built-in methods to manipulate strings, such as converting case, extracting substrings, finding substrings, and replacing substrings.

Examples of string methods:
const myString = "Hello, World!";

// Converting case
console.log(myString.toUpperCase()); // Output: "HELLO, WORLD!"
console.log(myString.toLowerCase()); // Output: "hello, world!"

// Extracting substrings
console.log(myString.slice(0, 5)); // Output: "Hello"
console.log(myString.substring(7, 12)); // Output: "World"
console.log(myString.substr(7, 5)); // Output: "World"

// Finding substrings
console.log(myString.indexOf("World")); // Output: 7 (index of the first occurrence)
console.log(myString.lastIndexOf("o")); // Output: 8 (index of the last occurrence)

// Replacing substrings
console.log(myString.replace("World", "Universe")); // Output: "Hello, Universe!"

Strings are fundamental to working with textual data in JavaScript, and understanding string manipulation methods is crucial for many types of applications, including web development and data processing.
""",
        'example': """"""
    },
    {
        'name': 'symbol',
        'define': """'Symbol' is a primitive data type introduced in ECMAScript 6 (ES6) to create unique and immutable values that can be used as object property keys. Symbols are used to prevent unintended property name collisions in objects and provide a level of privacy for object properties.

Creating Symbols:
Symbols are created using the 'Symbol()' function, which returns a unique symbol value.

Example of creating a symbol:
const mySymbol = Symbol();

Each symbol value is guaranteed to be unique, even if you create multiple symbols with the same description.

Example of creating symbols with the same description:
const symbol1 = Symbol('mySymbol');
const symbol2 = Symbol('mySymbol');

console.log(symbol1 === symbol2); // Output: false (each symbol is unique)

Using Symbols as Object Properties:
Symbols can be used as property keys in objects, providing a way to define "hidden" or "private" properties that are not accessible using normal object property access.

Example of using a symbol as an object property key:
const mySymbol = Symbol('mySymbol');
const myObject = {};

myObject[mySymbol] = 'Hello, Symbol!';
console.log(myObject[mySymbol]); // Output: "Hello, Symbol!"

Enumerating Object Properties with Symbols:
Symbols are not enumerable, which means they are not included when using 'for...in' loops or 'Object.keys()' to iterate through an object's properties.

Example of enumerating object properties excluding symbols:
const mySymbol = Symbol('mySymbol');
const myObject = {
    [mySymbol]: 'Hello, Symbol!',
    name: 'John',
    age: 30
};

for (const key in myObject) {
    console.log(key); // Output: "name", "age" (symbols are not included)
}

Retrieving Symbol Descriptions:
The description of a symbol can be obtained using the 'description' property of the symbol object.

Example of retrieving the description of a symbol:
const mySymbol = Symbol('mySymbol');
console.log(mySymbol.description); // Output: "mySymbol"

Built-in Symbols:
ES6 introduced several built-in symbols that have special meanings or behaviors. These symbols are used, for example, to define custom iterator methods, well-known method names, and more.

Example of using a built-in symbol:
const myIterableObject = {
    [Symbol.iterator]() {
        let count = 1;
        return {
            next() {
                return count <= 5 ? { value: count++, done: false } : { done: true };
            }
        };
    }
};

for (const item of myIterableObject) {
    console.log(item); // Output: 1, 2, 3, 4, 5
}

Symbols are a powerful tool for creating unique and private object properties, and they play a significant role in enhancing the functionality and security of JavaScript code.
""",
        'example': """"""
    },
    {
        'name': 'this',
        'define': """'this' is a special keyword in JavaScript that refers to the object on which the current code (function or method) is being executed. It provides a way to access the context or scope within which the code is running. The value of 'this' depends on how a function is called and not where it is defined.

The Value of 'this':
The value of 'this' can vary based on the function's invocation context:
1. Global Context: When 'this' is referenced in the global scope (outside any function or object), it refers to the global object (e.g., 'window' in browsers, 'global' in Node.js).

Example of 'this' in the global context:
console.log(this === window); // Output: true (in browsers)

2. Function Context: When 'this' is referenced inside a regular function (not an arrow function) that is called directly, 'this' also refers to the global object.

Example of 'this' in a regular function:
function myFunction() {
    console.log(this === window); // Output: true (in browsers)
}

myFunction();

3. Method Context: When 'this' is referenced inside a method (function within an object), 'this' refers to the object that owns the method.

Example of 'this' in a method:
const myObject = {
    name: 'John',
    sayHello() {
        console.log('Hello, ' + this.name + '!');
    }
};

myObject.sayHello(); // Output: "Hello, John!"

4. Constructor Context: When 'this' is referenced inside a constructor function (used with 'new' keyword to create objects), 'this' refers to the newly created object instance.

Example of 'this' in a constructor function:
function Person(name) {
    this.name = name;
}

const john = new Person('John');
console.log(john.name); // Output: "John"

Binding 'this' Manually:
The value of 'this' can be manually bound to a specific object using methods like 'bind()', 'call()', or 'apply()'.

Example of manually binding 'this':
const person = {
    name: 'John',
    greet() {
        console.log('Hello, ' + this.name + '!');
    }
};

const greetFunction = person.greet.bind(person);
greetFunction(); // Output: "Hello, John!"

Understanding 'this' is crucial for correctly accessing object properties and methods in various contexts in JavaScript.
""",
        'example': """"""
    },
    {
        'name': 'three.js',
        'trigger': 'three js',
        'define': """Three.js is a popular and powerful JavaScript library used for 3D computer graphics and web-based 3D animations. It provides a simple and straightforward API for creating, rendering, and animating 3D scenes in the browser using WebGL, a technology that enables hardware-accelerated rendering of 2D and 3D graphics.

Key Features of Three.js:
1. Scene and Object Creation: Three.js allows you to create a 3D scene, which acts as a container for all the 3D objects in the scene. You can create various types of 3D objects, including meshes, lights, cameras, and more.

Example of creating a 3D scene and a cube:
const scene = new THREE.Scene();

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);

scene.add(cube);
""",
        'example': """3D graphics in the browser using Three.js have become increasingly popular for creating interactive and visually appealing experiences. For more complex applications like games and simulations, Three.js offers a wide range of capabilities and tools for developers."""
    },
    {
        'name': 'typescript',
        'trigger': 'type script',
        'define': """TypeScript is a superset of JavaScript developed by Microsoft. It adds optional static typing and other advanced features to JavaScript, making it a more robust and scalable language for large-scale applications. TypeScript code is transpiled into standard JavaScript, ensuring compatibility with all modern browsers and environments.

Key Features of TypeScript:
1. Static Typing: TypeScript allows developers to specify types for variables, function parameters, and return values. This helps catch type-related errors during development and provides better code documentation.

Example of using static typing in TypeScript:
function add(a: number, b: number): number {
    return a + b;
}

const result = add(5, 10); // 'result' will be inferred as type 'number'

2. Interfaces: TypeScript introduces interfaces, which define the structure of objects. They enable better code organization and help prevent accidental property omissions or mismatches.

Example of using an interface in TypeScript:
interface Person {
    name: string;
    age: number;
}

function greet(person: Person): string {
    return 'Hello, ' + person.name;
}

const john: Person = { name: 'John', age: 30 };
console.log(greet(john)); // Output: "Hello, John"

3. Enumerations: TypeScript supports enumerations, which allow developers to define a set of named constants. This provides a more expressive and type-safe way to work with groups of related values.

Example of using an enumeration in TypeScript:
enum Color {
    Red,
    Green,
    Blue,
}

const selectedColor = Color.Green;
console.log(selectedColor); // Output: 1

4. Classes and Inheritance: TypeScript brings class-based object-oriented programming to JavaScript. Developers can define classes with constructors, methods, and properties, making code organization and reuse easier.

Example of using classes and inheritance in TypeScript:
class Animal {
    constructor(public name: string) {}
    makeSound() {
        console.log('Animal makes a sound');
    }
}

class Dog extends Animal {
    makeSound() {
        console.log('Dog barks');
    }
}

const dog = new Dog('Buddy');
dog.makeSound(); // Output: "Dog barks"

TypeScript's features improve code maintainability and provide a smoother development experience, especially in large projects with teams of developers.""",
        'example': """
            // Example of using TypeScript in a simple function
            function multiply(a: number, b: number): number {
                return a * b;
            }

            const result = multiply(5, 3);
            console.log(result); // Output: 15
        """
    },
    {
        'name': 'undefined',
        'define': """'undefined' is a primitive value in JavaScript that represents an uninitialized, non-existent, or missing value. It is one of the six primitive data types (undefined, null, boolean, number, string, symbol) and is automatically assigned to variables that are declared but not initialized or do not have a value.

Example of 'undefined':
let x;
console.log(x); // Output: undefined

In the above example, the variable 'x' is declared but not assigned a value, so it is automatically initialized with 'undefined'.

Use Cases of 'undefined':
1. Uninitialized Variables: When a variable is declared but not assigned a value, it is set to 'undefined' by default.

Example of an uninitialized variable:
let name;
console.log(name); // Output: undefined

2. Missing Object Properties: Accessing an object property that does not exist returns 'undefined'.

Example of accessing a non-existent property:
const person = { name: 'John', age: 30 };
console.log(person.address); // Output: undefined

3. Function Return: If a function does not explicitly return a value, it returns 'undefined' by default.

Example of a function without a return statement:
function greet() {
    console.log('Hello!');
}

const result = greet();
console.log(result); // Output: undefined

4. Function Arguments: If a function is called with fewer arguments than declared in the function definition, the missing arguments are set to 'undefined'.

Example of calling a function with fewer arguments:
function add(a, b) {
    return a + b;
}

const result = add(5);
console.log(result); // Output: NaN (Not a Number), as 'b' is undefined

Handling 'undefined':
Developers often use conditional statements or the 'typeof' operator to check if a variable is 'undefined' before using it, especially when working with optional values or function arguments.

Example of handling 'undefined':
function greet(name) {
    if (typeof name === 'undefined') {
        console.log('Hello, stranger!');
    } else {
        console.log('Hello, ' + name + '!');
    }
}

greet(); // Output: "Hello, stranger!"
greet('John'); // Output: "Hello, John!"

By understanding the behavior of 'undefined', developers can write more robust code and handle cases where values might be missing or not yet defined.""",
        'example': """
            // Example of checking for undefined before using a variable
            let age;
            if (typeof age === 'undefined') {
                console.log('Age is not defined.');
            } else {
                console.log('Age is: ' + age);
            }
        """
    },
    {
        'name': 'variable',
        'define': """A variable in JavaScript is a container used to store data values. Variables allow you to assign and access values throughout your code. JavaScript is a dynamically typed language, meaning variables can hold values of any data type, and their types can change during runtime.

Variable Declaration and Assignment:
To declare a variable in JavaScript, you use the 'var', 'let', or 'const' keyword, followed by the variable name and optionally an initial value.

Examples of variable declaration and assignment:
// Using 'var' (global scope)
var age = 30;

// Using 'let' (block scope)
let name = 'John';

// Using 'const' (block scope, read-only)
const pi = 3.14;

Variable Names:
Variable names can consist of letters, digits, underscores, and dollar signs. They must start with a letter, underscore, or dollar sign (not a digit). JavaScript is case-sensitive, so 'myVar' and 'myvar' are considered different variables.

Example of valid variable names:
let myVar = 42;
let _count = 10;
let $price = 20;

Variable Scope:
Variables can have either global scope or function/block scope, depending on where they are declared.

Global Scope: Variables declared outside of any function or block have global scope, meaning they are accessible from anywhere in the code, including within functions.

Example of a global variable:
var globalVar = 'I am global!';

function myFunction() {
    console.log(globalVar); // Output: "I am global!"
}

Function/Block Scope: Variables declared inside a function or block have function/block scope and are accessible only within that specific function or block.

Example of a function-scoped variable:
function myFunction() {
    var localVar = 'I am local!';
    console.log(localVar);
}

console.log(localVar); // Error: localVar is not defined

Variable Hoisting:
In JavaScript, variable declarations are hoisted to the top of their scope during the code execution phase. This means you can use a variable before declaring it, but its value will be 'undefined' until the assignment.

Example of variable hoisting:
console.log(myVar); // Output: undefined
var myVar = 42;

It's good practice to declare variables before using them to avoid unexpected behavior due to hoisting.

Constant Variables:
Variables declared with 'const' are read-only, meaning their values cannot be re-assigned once they are initialized. However, the contents of objects and arrays declared with 'const' can still be modified.

Example of a constant variable:
const pi = 3.14;
pi = 3.14159; // Error: Assignment to constant variable.

By using variables, JavaScript developers can efficiently manage data, perform computations, and create more dynamic and interactive applications.""",
        'example': """
            // Example of using variables in JavaScript
            let name = 'John';
            var age = 30;
            const PI = 3.14;

            console.log(name); // Output: "John"
            console.log(age); // Output: 30
            console.log(PI); // Output: 3.14
        """
    },
    {
        'name': 'vue',
        'trigger': 'vue js',
        'define': """Vue.js is a progressive JavaScript framework for building user interfaces (UIs) and single-page applications (SPAs). It is designed to be incrementally adoptable, allowing developers to integrate Vue.js into existing projects easily. Vue.js provides a robust and flexible ecosystem, making it a popular choice among front-end developers.

Key Features of Vue.js:
1. Declarative Rendering: Vue.js uses a template syntax that allows developers to declaratively render the UI based on the application's data state. The data and the DOM are automatically kept in sync, making it easy to build reactive applications.

Example of declarative rendering in Vue.js:
<div id="app">
    <p>{{ message }}</p>
</div>

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello, Vue.js!'
    }
});

2. Component-Based Architecture: Vue.js encourages building UIs using reusable and modular components. Each component encapsulates its logic, template, and styles, making code organization and maintenance more manageable.

Example of a Vue.js component:
Vue.component('my-component', {
    template: '<div>{{ message }}</div>',
    data() {
        return {
            message: 'Hello from Vue.js component!'
        };
    }
});

3. Directives: Vue.js provides built-in directives, such as 'v-if', 'v-for', and 'v-on', that allow developers to add dynamic behavior and interactivity to the HTML templates.

Example of using directives in Vue.js:
<div id="app">
    <p v-if="showMessage">{{ message }}</p>
    <button v-on:click="toggleMessage">Toggle Message</button>
</div>

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello, Vue.js!',
        showMessage: true
    },
    methods: {
        toggleMessage() {
            this.showMessage = !this.showMessage;
        }
    }
});

4. Vue Router: Vue.js provides an official routing library, Vue Router, that enables developers to implement client-side navigation and build SPAs with multiple views.

Example of using Vue Router:
// Main.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import Home from './components/Home.vue';
import About from './components/About.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About }
];

const router = new VueRouter({
    routes
});

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

5. Vuex: Vuex is Vue.js's official state management library, providing a centralized store for managing the application's state and enabling efficient communication between components.

Example of using Vuex:
// Store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        count: 0
    },
    mutations: {
        increment(state) {
            state.count++;
        }
    }
});

// Main.js
import Vue from 'vue';
import App from './App.vue';
import store from './store';

new Vue({
    store,
    render: h => h(App)
}).$mount('#app');

Vue.js is a versatile framework suitable for projects of all sizes, from small-scale applications to large enterprise-level SPAs. Its flexibility, performance, and ease of integration with other libraries have contributed to its rapid growth and popularity in the web development community.""",
        'example': """
            // Example of using Vue.js to create a simple component
            Vue.component('my-component', {
                template: '<div>{{ message }}</div>',
                data() {
                    return {
                        message: 'Hello from Vue.js component!'
                    };
                }
            });

            // Mount the component to the DOM
            new Vue({
                el: '#app'
            });
        """
    },
    {
        'name': 'webpack',
        'trigger': 'web pack',
        'define': """Webpack is a popular module bundler for JavaScript applications. It takes the various modules and assets in a project, such as JavaScript files, CSS styles, and images, and transforms them into optimized bundles suitable for deployment in the browser. Webpack simplifies the process of managing dependencies and improves the performance of web applications.

Key Features of Webpack:
1. Module Bundling: Webpack treats all code and assets in the project as modules, even JavaScript files, CSS styles, and images. It bundles these modules into a smaller number of files, reducing the number of HTTP requests and improving page load times.

Example of module bundling with Webpack:
// webpack.config.js
module.exports = {
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    }
};

2. Loaders: Webpack uses loaders to process different types of files during the bundling process. Loaders enable developers to transform files from one format to another, apply transpilation, and perform various optimizations.

Example of using loaders in Webpack for processing CSS files:
// webpack.config.js
module.exports = {
    // ...
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'style-loader', // Inject CSS into the DOM
                    'css-loader' // Handle CSS imports
                ]
            }
        ]
    }
};

3. Plugins: Webpack plugins extend the bundling process with additional functionalities and optimizations. Plugins can be used for tasks such as code minification, environment variable injection, and code splitting.

Example of using a plugin in Webpack for code minification:
// webpack.config.js
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    // ...
    optimization: {
        minimize: true,
        minimizer: [new TerserPlugin()] // Minify JavaScript
    }
};

4. Code Splitting: Webpack enables code splitting, allowing developers to split the application's code into multiple smaller chunks. This feature is beneficial for large applications as it reduces the initial loading time and improves overall performance.

Example of code splitting in Webpack:
// webpack.config.js
module.exports = {
    // ...
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    }
};

5. Development Server: Webpack provides a built-in development server that allows developers to test and preview the application locally without deploying it to a production server.

Example of using Webpack development server:
// webpack.config.js
module.exports = {
    // ...
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        port: 8080
    }
};

6. Asset Management: Webpack supports various file formats, such as images, fonts, and videos, making it easy to handle static assets and include them in the bundles.

Example of asset management in Webpack:
// webpack.config.js
module.exports = {
    // ...
    module: {
        rules: [
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    'file-loader' // Handle image imports
                ]
            }
        ]
    }
};

Webpack is widely used in modern JavaScript development, especially in projects that use frameworks like React, Vue.js, or Angular. Its extensive range of features and active community support make it an essential tool for building efficient and well-organized web applications.""",
        'example': """
            // Example of using Webpack to bundle JavaScript modules
            // webpack.config.js
            const path = require('path');

            module.exports = {
                entry: './src/index.js',
                output: {
                    filename: 'bundle.js',
                    path: path.resolve(__dirname, 'dist')
                }
            };
        """
    },
    {
        'name': 'yarn',
        'define': """Yarn is a fast, secure, and reliable package manager for JavaScript. It was developed by Facebook and is designed to be an alternative to npm (Node Package Manager). Yarn simplifies the process of managing dependencies, ensuring consistent installations, and speeding up package downloads.

Key Features of Yarn:
1. Dependency Management: Yarn helps manage project dependencies by automatically generating and updating a 'yarn.lock' file. This file ensures that the exact versions of dependencies are installed, guaranteeing consistency across different development environments.

Example of using Yarn to install project dependencies:
// Terminal
yarn install

2. Speed and Performance: Yarn is built with performance in mind. It uses a caching mechanism to speed up package installations, which results in faster overall development workflows.

Example of using Yarn to install packages with caching:
// Terminal
yarn add lodash

3. Workspaces: Yarn supports a feature called workspaces, which allows developers to manage multiple related packages within a single repository. This feature is beneficial for monorepo setups and complex projects.

Example of using Yarn workspaces:
// package.json
{
    "private": true,
    "workspaces": [
        "packages/*"
    ]
}

4. Scripts: Yarn allows developers to define custom scripts in the 'package.json' file. These scripts can be used to automate various tasks, such as building, testing, and deploying the project.

Example of using Yarn scripts in 'package.json':
// package.json
{
    "scripts": {
        "start": "webpack --mode development",
        "build": "webpack --mode production",
        "test": "jest"
    }
}

5. Easy Upgrades: Yarn provides commands to update packages easily, either to their latest versions or to specific versions specified in the 'package.json' file.

Example of using Yarn to update packages:
// Terminal
yarn upgrade

6. Offline Mode: Yarn includes an offline mode, allowing developers to install packages without an internet connection, provided the packages have been cached previously.

Example of using Yarn offline mode:
// Terminal
yarn install --offline

Yarn has gained significant popularity among JavaScript developers due to its speed, reliability, and powerful features. It continues to be a preferred choice for managing dependencies and improving development workflows in modern JavaScript projects.""",
        'example': """
            // Example of using Yarn to install packages
            // Terminal
            yarn add lodash

            // Example of using Yarn scripts to run development server
            // package.json
            {
                "scripts": {
                    "start": "webpack-dev-server --mode development"
                }
            }
        """
    },
    {
        'name': 'Array',
        'define': """In JavaScript, an 'Array' is a special data structure that allows you to store a collection of elements, such as numbers, strings, objects, or even other arrays. Arrays are ordered, meaning the elements have a specific position, and you can access and modify them using their index.

Arrays in JavaScript can dynamically resize, meaning you can add or remove elements as needed. The size of an array is not fixed like in some other programming languages.

Example (Defining and using an Array):
// Defining an array with different types of elements
let myArray = [1, 'hello', true, { name: 'John' }];

// Accessing elements in the array using index
console.log(myArray[0]); // Output: 1
console.log(myArray[1]); // Output: 'hello'
console.log(myArray[2]); // Output: true

// Modifying elements in the array
myArray[3] = { name: 'Jane' };
console.log(myArray[3]); // Output: { name: 'Jane' }

// Array length (number of elements in the array)
console.log(myArray.length); // Output: 4


Some commonly used Array Methods include:
1. 'push()': Adds one or more elements to the end of an array and returns the new length of the array.
2. 'pop()': Removes the last element from an array and returns that element.
3. 'shift()': Removes the first element from an array and returns that element. The remaining elements' indices are shifted to lower positions.
4. 'unshift()': Adds one or more elements to the beginning of an array and returns the new length of the array.
5. 'splice()': Adds or removes elements from an array at a specified index.
6. 'concat()': Combines two or more arrays and returns a new array.
7. 'slice()': Extracts a section of an array and returns a new array without modifying the original array.
8. 'indexOf()': Searches for an element in an array and returns its index. Returns -1 if the element is not found.
9. 'lastIndexOf()': Searches for an element in an array from the end and returns its index. Returns -1 if the element is not found.
10. 'includes()': Checks if an array includes a specific element and returns a boolean value.

""",
        'example': """
            // Example 1:
            // Defining an array with different types of elements
            let myArray = [1, 'hello', true, { name: 'John' }];

            // Accessing elements in the array using index
            console.log(myArray[0]); // Output: 1
            console.log(myArray[1]); // Output: 'hello'
            console.log(myArray[2]); // Output: true

            // Modifying elements in the array
            myArray[3] = { name: 'Jane' };
            console.log(myArray[3]); // Output: { name: 'Jane' }

            // Array length (number of elements in the array)
            console.log(myArray.length); // Output: 4
        """
    },
    {
        'name': 'every',
        'define': """'every' is a higher-order array method that tests whether all elements in the array pass a given condition (predicate) implemented by a callback function. It returns a boolean value, 'true' if all elements satisfy the condition, otherwise 'false'.

The 'every' method stops iterating and returns 'false' immediately when it encounters an element that does not meet the condition, making it efficient for certain use cases.

Example (Using every to check if all numbers are positive):
let numbers = [1, 2, 3, 4, 5];

let allPositive = numbers.every(function(number) {
    return number > 0;
});

console.log(allPositive); // Output: true
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];

            let allPositive = numbers.every(function(number) {
                return number > 0;
            });

            console.log(allPositive); // Output: true
        """
    },
    {
        'name': 'some',
        'define': """'some' is a higher-order array method that tests whether at least one element in the array passes a given condition (predicate) implemented by a callback function. It returns a boolean value, 'true' if at least one element satisfies the condition, otherwise 'false'.

The 'some' method stops iterating and returns 'true' immediately when it encounters an element that meets the condition, making it efficient for certain use cases.

Example (Using some to check if any number is even):
let numbers = [1, 2, 3, 4, 5];

let hasEvenNumber = numbers.some(function(number) {
    return number % 2 === 0;
});

console.log(hasEvenNumber); // Output: true
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];

            let hasEvenNumber = numbers.some(function(number) {
                return number % 2 === 0;
            });

            console.log(hasEvenNumber); // Output: true
        """
    },
    {
        'name': 'filter',
        'define': """'filter' is a higher-order array method that creates a new array containing elements from the original array that pass a given condition (predicate) implemented by a callback function. It returns an array with only the elements that satisfy the condition.

The 'filter' method does not modify the original array, and it returns a new array with the selected elements.

Example (Using filter to get even numbers from an array):
let numbers = [1, 2, 3, 4, 5];

let evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});

console.log(evenNumbers); // Output: [2, 4]
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];

            let evenNumbers = numbers.filter(function(number) {
                return number % 2 === 0;
            });

            console.log(evenNumbers); // Output: [2, 4]
        """
    },
    {
        'name': 'reduce',
        'define': """'reduce' is a higher-order array method that iterates through the array and accumulates a single value based on the elements in the array and a provided callback function. It "reduces" the array to a single value.

The callback function takes two arguments: the accumulator (the result of previous iterations) and the current element in the array. It returns the updated accumulator value for the next iteration.

Example (Using reduce to find the sum of numbers in an array):
let numbers = [1, 2, 3, 4, 5];

let sum = numbers.reduce(function(accumulator, currentNumber) {
    return accumulator + currentNumber;
}, 0);

console.log(sum); // Output: 15
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];

            let sum = numbers.reduce(function(accumulator, currentNumber) {
                return accumulator + currentNumber;
            }, 0);

            console.log(sum); // Output: 15
        """
    },
    {
        'name': 'find',
        'define': """'find' is a higher-order array method that returns the value of the first element in the array that satisfies a given condition (predicate) implemented by a callback function. It returns 'undefined' if no element satisfies the condition.

The 'find' method stops iterating and returns the first element that meets the condition, making it efficient for certain use cases.

Example (Using find to get the first even number from an array):
let numbers = [1, 2, 3, 4, 5];

let firstEvenNumber = numbers.find(function(number) {
    return number % 2 === 0;
});

console.log(firstEvenNumber); // Output: 2
""",
        'example': """
            // Example 1:
            let numbers = [1, 2, 3, 4, 5];

            let firstEvenNumber = numbers.find(function(number) {
                return number % 2 === 0;
            });

            console.log(firstEvenNumber); // Output: 2
        """
    },
    {
    'name': 'Microservices Architecture',
    'trigger': 'micro services',
    'define': """Microservices Architecture is an architectural style used in software development that structures an application as a collection of small, independent, and loosely coupled services. Each service is responsible for a specific business capability and can be developed, deployed, and scaled independently. Microservices aim to break down a monolithic application into smaller, manageable components, allowing teams to work on individual services independently, facilitating faster development and deployment cycles.

Microservices communicate with each other through well-defined APIs, often using lightweight protocols like HTTP/REST or messaging systems like RabbitMQ or Apache Kafka. This decentralized communication enables services to evolve and scale independently without affecting the entire application.

Key Characteristics of Microservices Architecture:
1. Decentralization: Each microservice is an autonomous unit that can be developed and deployed independently, promoting decentralized decision-making and development.
2. Loosely Coupled: Microservices are designed to have minimal dependencies on other services, reducing the impact of changes and allowing for flexible deployments.
3. Single Responsibility: Each service focuses on a specific business capability or feature, adhering to the Single Responsibility Principle.
4. Independent Scalability: Services can be scaled individually based on their specific demand, optimizing resource utilization.
5. Technology Diversity: Microservices allow the use of different programming languages, frameworks, and databases for each service based on its requirements.
6. Resilience: Failure in one service should not cascade to other services, as they are designed to be resilient and handle failures gracefully.
7. Continuous Delivery: Microservices encourage automated deployment and continuous delivery practices, streamlining the software development process.
8. Containerization: Services are often deployed in containers like Docker, providing consistency and portability across different environments.
9. Observability: Monitoring, logging, and tracing are essential in a microservices architecture to gain insights into the behavior and performance of services.
10. Evolutionary Design: Microservices promote evolutionary design, allowing the application to adapt to changing business needs over time.

It's essential to note that while microservices offer several benefits, they also introduce additional complexities, such as managing inter-service communication, dealing with eventual consistency, and ensuring data integrity across services. Proper planning and infrastructure are required to implement and maintain a successful microservices architecture in a real-world application.""",
    'example': """N/A - Microservices architecture is an architectural style, and examples would require designing and implementing a complete microservices-based application, which is beyond the scope of a simple code snippet."""
},
{
        'name': 'Primitives',
        'trigger': 'javascript primitives',
        'define': """JavaScript Primitives are the basic data types in JavaScript that represent single values. There are six primitive data types in JavaScript: 
        1. Number: Represents numeric values, including integers and floating-point numbers.
        2. String: Represents sequences of characters enclosed in single ('') or double ("") quotes.
        3. Boolean: Represents true or false values for logical operations.
        4. Undefined: Represents a variable that has been declared but not assigned a value.
        5. Null: Represents the intentional absence of any object value.
        6. Symbol: Represents unique, immutable values that are often used as object property keys to avoid name collisions.

Primitive values are immutable, meaning their values cannot be changed once they are created. When you assign a primitive value to a variable or pass it as an argument to a function, you are working with a copy of the actual value rather than a reference to it.""",
        'example': """
            // Examples of JavaScript Primitives
            const numberValue = 42; // Number
            const stringValue = 'Hello, World!'; // String
            const booleanValue = true; // Boolean
            let undefinedValue; // Undefined
            const nullValue = null; // Null

            // Example of using Symbol
            const symbolValue = Symbol('mySymbol');
        """
    },
    {
        'name': 'Objects',
        'trigger': 'javascript objects',
        'define': """JavaScript Objects are complex data types used to store collections of key-value pairs. They represent entities with properties and behaviors. Objects are one of the fundamental building blocks in JavaScript, and almost everything in JavaScript is an object or behaves like one. Objects are used to model real-world entities and abstract data structures.

In JavaScript, objects are defined using curly braces {} and consist of properties, where each property has a name (key) and a value. The value of a property can be a primitive value, another object, or a function (in which case, the property is called a method).

Unlike primitives, objects are mutable, which means their properties can be modified after creation. However, when you assign an object to a variable or pass it as an argument to a function, you are working with a reference to the object, not a copy of its value. Modifying an object's property through one reference affects all other references to that object.""",
        'example': """
            // Example of JavaScript Objects
            const person = {
              name: 'John Doe',
              age: 30,
              city: 'New York',
              hobbies: ['reading', 'coding', 'swimming'],
              address: {
                street: '123 Main St',
                zipCode: '10001',
              },
              sayHello: function() {
                console.log('Hello, I am ' + this.name);
              },
            };

            console.log(person.name); // Output: 'John Doe'
            console.log(person.hobbies[1]); // Output: 'coding'
            person.age = 31; // Modifying a property
            person.sayHello(); // Output: 'Hello, I am John Doe'

            // Example of object reference
            const personReference = person; // Creating a reference
            personReference.name = 'Jane Doe'; // Modifying the object through the reference
            console.log(person.name); // Output: 'Jane Doe' (as the object was modified through the reference)
        """
    },
    {
        'name': 'microservices',
        'trigger': 'micro services',
        'define': """Microservices, also known as the microservices architecture, is an architectural style that structures an application as a collection of loosely coupled services. In a microservices architecture, services should be fine-grained, and the protocols should be lightweight. The benefit of decomposing an application into different smaller services is that it improves modularity and makes the application easier to understand, develop, and test.

The core principles of microservices are:

1. Single Responsibility:
Each microservice should have a single responsibility and should do that task well. This concept is similar to the Single Responsibility Principle from SOLID principles in object-oriented design.

2. Business-Centric:
Each microservice should represent a small business capability. This allows the team to focus on one area of the business at a time.

3. Autonomy:
Microservices can be developed, deployed, scaled, and even taken down independently without affecting the whole system.

4. Decentralized Governance:
There is no need for a centralized governing body, and each microservice can use its own technique and technology, best suited for its requirement.

5. Failure Isolation:
Failure in one microservice should not affect other services or the entire application.

6. Continuous Delivery:
Each microservice can be managed by a small team who takes care of the lifecycle, from development, testing, deployment to monitoring, and maintenance.

7. Infrastructure Automation:
With the help of containerization (like Docker) and orchestration tools (like Kubernetes), microservices can be easily automated for deployment, scaling, and recovery.

The advantages of using microservices are:

Independence: Individual components can evolve independently, reducing the coordination overhead in project management.
Scalability: Different components have different resource requirements, and this can be a much more cost-effective way to scale the application.
Resilience: If a single component failure were to occur, the rest of the application can potentially continue to function.
Reusability: Components can be reused across different projects.
However, there are also challenges:

Inter-Service Communication: The various services need to communicate. This communication framework needs to be robust and efficient. Typically, APIs are used for this purpose.
Data Consistency: Each service has its own database to ensure loose coupling. Managing consistency across services is a challenge.
Testing and Deployment: Writing effective tests for microservices-based applications can be complex, as can deploying a multi-service application.
        """,
        'example':''
    },
    
     ]
     }