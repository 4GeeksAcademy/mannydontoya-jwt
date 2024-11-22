import React, { useState, useEffect, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { Context } from "../store/appContext";

export const Private = () => {
    const { store, actions } = useContext(Context);
    const navigate = useNavigate()
    useEffect(() => {
        console.log("token", localStorage.getItem("token"))
        axios.get(process.env.BACKEND_URL + "/private",
            { "content-type": "application/json", "headers": { "Authorization": "Bearer " + localStorage.getItem("token") } })
            .catch(error => {
                navigate("/login")
                // localStorage.clear()
            })
    }, [])
    return (
        <div className="container">
            <h1>Private</h1>
        </div>
    );
};
