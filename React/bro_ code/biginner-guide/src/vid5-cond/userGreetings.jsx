import PropTypes, { bool, string } from "prop-types";

function UserGreeting(props) {

    const welcomeMessage = <h2 className="welcome-message">Welcom {props.username} </h2>
    const loginprompt = <h2 className="login-prompt"> Please log in to continue </h2>
     
    // Turnary operator
    return (props.isLoggenIn ? welcomeMessage : loginprompt);

    /*  Basic implementation
    if (props.isLoggedIn){
        return <h2 className="welcome-message">Welcom {props.username} </h2>
    }
    else {
        return <h2 className="login-prompt"> Please log in to continue </h2>
    }*/
}

UserGreeting.prototype = {
    isLoggenIn: PropTypes.bool,
    username: PropTypes.string,
}
UserGreeting.defaultProps = {
    isLoggenIn: false,
    username: "Guest",
}

export default UserGreeting