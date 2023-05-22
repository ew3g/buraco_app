import { React, useState, useEffect, useRef } from "react";
import 'leaflet/dist/leaflet.css';

import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet'
import L from 'leaflet';

import { getBuracos, votoBuraco, createBuraco } from "../api/buraco";
import { getTamanhosBuraco } from "../api/tamanhoBuraco";


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
    const [tamanhosBuraco, setTamanhosBuraco] = useState([])

    const [tamanhoBuracoSelecionado, setTamanhoBuracoSelecionado] = useState('')

    const [markerPosition, setMarkerPosition] = useState(null)

    useEffect(() => {
        const fetchBuracos = async () => {
            const data = await getBuracos();
            console.log(data);
            setBuracos(data)
        };

        const fetchTamanhosBuraco = async () => {
            const data = await getTamanhosBuraco();
            console.log(data);
            setTamanhosBuraco(data);
        }

        fetchBuracos();
        fetchTamanhosBuraco();
    }, []);


    async function handleVotoBuraco(buracoId) {
        const data = await votoBuraco(buracoId);
        console.log(data)
        window.location.reload(false);
    }


    const handleMapClick = (event) => {
        setMarkerPosition(event.latlng)
    }

    const handleMarkerConfirm = async () => {
        const lat = markerPosition.lat;
        const lng = markerPosition.lng;

        console.log(markerPosition);
        if (!checkSeDentroDeGuarulhos(lat, lng)) {
            alert('O buraco deve estar dentro dos limites da cidade de Guarulhos!');
            return;
        }

        const request = {
            "latitude": lat.toString(),
            "longitude": lng.toString(),
            "tamanho_buraco_id": Number(tamanhoBuracoSelecionado),
            "usuario_id": Number(localStorage.getItem('usuarioId')),
        }
        console.log(request);
        const data = await createBuraco(request);
        console.log(data);

        setMarkerPosition(null);
        window.location.reload(false);

    }

    const checkSeDentroDeGuarulhos = (latitude, longitude) => {
        const guarulhosBounds = {
            north: -23.367433,
            south: -23.516082,
            west: -46.570909,
            east: -46.373725
        };

        if (
            latitude >= guarulhosBounds.south &&
            latitude <= guarulhosBounds.north &&
            longitude >= guarulhosBounds.west &&
            longitude <= guarulhosBounds.east
        ) {
            return true;
        }

        return false;
    }


    function MapClickHandler() {
        useMapEvents({
            click: handleMapClick,
        });
        return null;
    }


    const PopupMarker = (props) => {
        const leafletRef = useRef();
        useEffect(() => {
            leafletRef.current.openPopup();
        }, [])
        return <Marker ref={leafletRef} {...props} />
    }


    const handleTamanhoBuracoSelectChange = (event) => {
        console.log(event.target.value);
        setTamanhoBuracoSelecionado(event.target.value);
    }


    const position = [-23.455, -46.533]

    return (
        <MapContainer center={position} zoom={13} scrollWheelZoom={true} style={{ height: "100vh", width: "100%" }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <MapClickHandler />
            {markerPosition && (
                <PopupMarker position={markerPosition} icon={markerIcon("blue")}>
                    <Popup>
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12">
                                    <span> Deseja cadastrar um buraco aqui?</span>
                                </div>
                                <br /><br />
                                <div className="row">
                                    <div className="col-md-12">
                                        <select className="form-select" value={tamanhoBuracoSelecionado} onChange={handleTamanhoBuracoSelectChange}>
                                            <option value="null">Tamanho do Buraco</option>
                                            {tamanhosBuraco.map(tamanhoBuraco => (
                                                <option key={tamanhoBuraco.id} value={tamanhoBuraco.id}>
                                                    {tamanhoBuraco.nome}
                                                </option>
                                            ))}
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <br />
                            <div className="row">
                                <div className="col-md-12">
                                    <button className="btn btn-primary" onClick={handleMarkerConfirm}>Confirmar</button>
                                </div>
                            </div>
                        </div>
                    </Popup>
                </PopupMarker>
            )}
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