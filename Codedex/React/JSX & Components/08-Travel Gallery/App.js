export default function App() {
    const barcelonaImage = <img src={"https://i.imgur.com/qaQNzqi.png"}  alt="Barcelona" />;
    const tokyoImage = <img src={"https://i.imgur.com/OAx1wzO.png"}  alt="Tokyo" />;
    const ohioImage = <img src={"https://i.imgur.com/CxJjltu.png"}  alt="Ohio" />;
    const imageGallery = [barcelonaImage, tokyoImage, ohioImage]
    const list =
        <li className="list">
            {imageGallery[0]}
            {imageGallery[1]}
            {imageGallery[2]}
        </li>
    return (
        <ul>
            {list}
        </ul>)
}
