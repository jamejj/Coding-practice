export default function App() {
    // const catalogItems = array of objects here 💖
    const catalogItems = [
        {
            name: "Dan",
            category: "Developer",
            website: "dandeveloper.dev"
        }
    ]
    return <div>
        {catalogItems.map(function (item) {
            return (
                <div>
                    <h2>{item.name}</h2>
                    <h3>Specialty: {item.category}</h3>
                    <a href={item.category}>Learn more</a>
                </div>
            )
        })}
    </div>
}
