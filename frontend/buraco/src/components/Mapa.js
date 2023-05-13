import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

const Mapa = () => {
    const [marcador, setMarcador] = useState(null);

    const handleClick = (event) => {
        const { lat, lng } = event.latlng;
        setMarcador({ lat, lng });
    };

    return (
        <MapContainer
            center={[-23.455, -46.533]}
            zoom={15}
            scrollWheelZoom={false}
            style={{ height: "500px", width: "100%" }}
            onclick={handleClick}
        >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {marcador && (
                <Marker position={[marcador.lat, marcador.lng]}>
                    <Popup>Um buraco aqui</Popup>
                </Marker>
            )}
        </MapContainer>
    );
};

export default Mapa;