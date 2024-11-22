import { Link } from "react-router-dom";
import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const token = localStorage.getItem("token")
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					{!store.token && <Link to="/signup">
						<button className="btn btn-primary">Signup</button>
					</Link>}
					{!store.token && <Link to="/login">
						<button className="btn btn-primary">Login</button>
					</Link>}
					{store.token && <Link to="/login">
						<button onClick={actions.logout} className="btn btn-primary">Logout</button>
					</Link>}
				</div>
			</div>
		</nav>
	);
};
