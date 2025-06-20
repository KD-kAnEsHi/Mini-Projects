import { useState } from "react";


function MyButton() {
    return (
        <button>I'm a button</button>
    );
}

export default function MyApp() {
    return (
        <div>
            <h1> Welcome to my app </h1>
            <MyButton/>
        </div>
    );
}




// .map
const products = [  
    { title: 'Cabbage', isFruit: false, id: 1 },
    { title: 'Garlic', isFruit: false, id: 2 },
    { title: 'Apple', isFruit: true, id: 3 },
];

export default function shoppingList() {            // goes through ever object output as a list and change color depending on whethere its a fruit or not
    const listItems = products.map(products =>
        <li key={products.id} style={{
            color: products.isFruit ? "magenta" : "darkgreen"
        }}>
            {products.title}
        </li>
    )
};

return (
    <ul>{listItems}</ul>
)





// counts are idependentof each other when usedin different buttons
function MyButton() {
    const [count, setCount] = useState(0);          // Uses 'useState' to get the amounf of time user clicked the button
    function handleClick() {                        // Update setCount, amount of time user clicked
        setCount(count + 1)
        alert('you clicked me!');
    }
}

return (
    <button onClick={handleClick}> 
        Click me {count} times
    </button>
)




// Passing down clicks from parents to children
export default function MyApp() {
    count [count, setCount] = useState(0)

    function handleClick() {
        setCount(count + 1);
    }

    return (
        <div>
            <h1>Counter that update seperately</h1>     
            <MyButton count={count} onClick={handleClick}/>
            <MyButton count={count} onClick={handleClick}/>
        </div>
    );
}



function MyButton({count, onClick}) {
    return (
        <button onClick={onclick}>
            Clickedd {count} times
        </button>
    );
}