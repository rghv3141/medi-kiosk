import React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

function Header() {
	let style = {
		width: '100vw',
		height: '100px',
		border: '2px solid black',
		borderRadius: '15px',
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
	};

	return (
		<div style={style}><h1> MediAssist </h1></div>
	);
}

export function Homecontent() {
	return(
		<>
		<div><h2> Select Language </h2></div>
		<div style={{display: 'flex', width: '100vw', justifyContent: 'center', gap: '20px', flexDirection: 'row'}}>
		<Card sx={{ minWidth: 275 }}>
		<CardContent>
			English
		</CardContent>
		<CardActions>
			<Button size="small">choose</Button>
		</CardActions>
		</Card>
		<Card sx={{ minWidth: 275}}>
		<CardContent>
			Hindi
		</CardContent>
		<CardActions>
			<Button size="small">choose</Button>
		</CardActions>
		</Card>
		</div>
		</>
	);
}
export default Header;

