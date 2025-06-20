import PropTypes from 'prop-types';     // needed to use propTypes

// props - passing variable and using props, to select the ouptput
function Student(props) {
    return (
        <div className="student">
            <p>Name: {props.name} </p>
            <p>Age: {props.age} </p>
            <p>Student: {props.isStudent ? "Yes" : "No"} </p>
        </div>
    );
}


// propsTypes - use for makign sure user inputter correct varaibles
Student.propTypes = {
    name: PropTypes.string,
    age:  PropTypes.number,
    isStudent: PropTypes.bool,
}


// defaultProps - default values when no values is sent by the user
Student.defaultProps = {
    name: "Guest",
    age: 0,
    isStudent: false,
}

export default Student