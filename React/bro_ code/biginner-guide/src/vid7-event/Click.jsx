

function Click() {
/*
    let count = 0;
    const handleClick = () => console.log("NONONONO");
    const handleClick2 = (name) =>{
        if (count < 3){
            count++;
             console.log(`${name} you clicked me ${count} too much`);
        }
        else{
             console.log(`${name} stop clicking`);
        }
    };
*/

    const handleClick = (e) => e.target.textcontect = "Stop Ouch";

    return (
       // <button onClick={handleClick2("loce")}>Click</button>         // This calls the function after you load the bace due to the passed argument
       //   <button onClick={() => handleClick2("pop")}>Click</button>    // If user clcisk then display message on screen
        
        <button onClick={(e) => handleClick(e)} >CLick ME</button>
    )
}
export default Click