import { func } from 'prop-types';
import React, {useState} from 'react';

function MyComponent() {
    const [name, setName] = useState("");
    const [quantity, setQuantity] = useState(1)
    const [comment, setComment] = useState("");
    const [payment, setPayment] = useState("")

    function handleNameChnage(event) {
        setName(event.target.value);            // changes name with user inputs
    }

    function handleQuantityChange(event) {
        setQuantity(event.target.value);
    }

    function handleCommentChange(event){
        setComment(event.target.value);
    }

    function handlePaymentChange(event){
        setPayment(event.target.value);
    }

    return (
        <div>
            <input value={name} onChange={handleNameChnage}></input>
            <p>Name: {name}</p>

            <input value={quantity} onChange={handleQuantityChange} type="number"/>
            <p>Quantity: {quantity}</p>

            <textarea value={comment} onChange={handleCommentChange} placeholder="Enter delivery intructions" />
            <p>Comment: {comment} </p>

            <select value={payment} onChange={handlePaymentChange}>
                <option value="" >Select and Option</option>
                <option value="Visa" >Visa</option>
                <option value="Master Card" >Master Card</option>
                <option value="Gift Card" >Gift Card</option>
            </select>
            <p>Payment: {payment} </p>

        </div>
    )
}
export default MyComponent