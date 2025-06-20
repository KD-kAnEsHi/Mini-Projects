// import style from './Button.module.css'

function Button() {

    // Inline CSS Styling
    const styles = {
        backgroundColor:" hsl(200, 100%, 50%)",
        color: "white",
        padding: "10px 20px",
        borderRadius: "5px",
        border: "none",
        cursor: "pointer",
    }

    // Module CSS Styling, get the CSS styling from the 'Button.modules.css'
    // return (<button className={style.button}>Click me</button>);

    // Inline CSS Styling, get the CSS from a 'const variable'
    // great for use only a few components and with minimal styling
    return (<button style={styles}>Click me</button>);
}

export default Button