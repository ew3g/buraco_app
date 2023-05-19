import { React, useState, useEffect } from "react";
import 'leaflet/dist/leaflet.css';

import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet'
import L from 'leaflet';

import { getBuracos, votoBuraco } from "../api/buraco";




const text = L.divIcon({ html: 'Your HTML text here' });


const markerIcon = (color) => {

    var iconUrl = `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${color}.png`
    return L.icon({
        iconUrl: iconUrl,
        iconSize: [32, 48],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32],
    });
}


const Mapa = () => {
    const [buracos, setBuracos] = useState([]);

    useEffect(() => {
        const fetchBuracos = async () => {
            const data = await getBuracos();
            console.log(data);
            setBuracos(data)
        };
        fetchBuracos();
    }, []);


    async function handleVotoBuraco(buracoId) {
        const data = await votoBuraco(buracoId);
        console.log(data)
        window.location.reload(false);
    }


    const handleMapClick = (event) => {
        console.log(event);
        console.log("clicou");
        const { lat, lng } = event.latlng;
        console.log(lat, lng);
    }

    function MapClickHandler() {
        useMapEvents({
            click: handleMapClick,
        });
        return null;
    }

    const position = [-23.455, -46.533]

    return (
        <MapContainer center={position} zoom={13} scrollWheelZoom={true} style={{ height: "100vh", width: "100%" }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <MapClickHandler />
            {buracos.map((buraco) => (
                <Marker key={buraco.id} position={[buraco.latitude, buraco.longitude]} icon={markerIcon(buraco.cor)}>
                    <Popup>
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12">
                                    <span>Tamanho: {buraco.tamanho}</span>
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-md-12">
                                    <span>Votos: {buraco.votos}</span>
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-md-12">
                                    <button className="btn btn-danger" onClick={() => handleVotoBuraco(buraco.id)}>Votar</button>
                                </div>
                            </div>


                        </div>
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

export default Mapa;