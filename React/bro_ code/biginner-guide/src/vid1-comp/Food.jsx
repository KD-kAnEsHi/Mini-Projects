
function Food() {
    const food1 = "orange";
    const food2 = "banana";

    return(
        <ul>
            <li>Apple</li>
            <li>{food2}</li>
            <li>{food1.toUpperCase()}</li>
        </ul>
    );
}

export default Food