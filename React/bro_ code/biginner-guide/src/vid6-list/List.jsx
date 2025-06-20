

function List() {
    // const fruits = ["apple", "orange", "banana", "coconut", "pineaple"]
    // const listitems = fruits.map(fruits => <li>fruit</li>); // Adds every item in the lists into an a <li>

    const fruits = [{id: 1, name: "apple", calories: 95},
                    {id: 2, name: "banana", calories: 65},
                    {id: 3, name: "orange", calories: 105},
                    {id: 4, name: "pineaple", calories: 60},
                    {id: 5, name: "goyava", calories: 55}
    ];

    fruits.sort((a, b) => a.name.localeCompare(b.name));    // Sort in alphebetical order
    fruits.sort((a, b) => b.name.localeCompare(a.name));    // Sort in reverse

    fruits.sort((a, b) => a.calories - b.calories);         // Numeric sort
    fruits.sort((a, b) => b.calories - a.calories);         // Reverse numeric sort
    const listitems = fruits.map(fruit => <li key={fruit.id}>{fruit.name}: &nbsp;
                                                        <b>{fruit.calories}</b></li>)

    const lowcalFruit = fruits.filter(fruit => fruit.calories < 100);    // added fruits wiht <100 cal in lowcalFruit list
    const listitems2 = fruits.map(lowcalFruit => <li key={lowcalFruit.id}>{lowcalFruit.name}: &nbsp;
                                                        <b>{lowcalFruit.calories}</b></li>)
    return (<>
            <ul>{listitems}</ul>
            <ul>{listitems2}</ul>
        </>);
}
export default List