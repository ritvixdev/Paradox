// React: Sorting Aticle

// File: components; File:App

// ...

function App ({articles}) {

    const [articleList, setArticleList] = useState(articles);

    const sortByUpvote = () => {
        let newArticle = []
        // Object.assign to create a copy of the source object to the target
        Object.assign(newArticle, articleList)
        newArticle.sort((a,b) => {
            if(a.upvotes >b.upvotes){
                return -1
            }
            if(a.upvotes < b.upvotes){
                return 1
            }
            return 0
        })

        setArticleList(newArticle);
    }

    const sortByDate = () => {
        let newArticle = []
        Object.assign(newArticle, articleList)
        newArticle.sort((a,b) => {

            const aDate = new Date(a.date);
            const bDate = new Date(a.date);

            if(aDate > bDate){
                return -1
            }
            if(aDate < bDate){
                return 1
            }
            return 0
        })

        setArticleList(newArticle);
    }

    return (
        <div>
            <button onClick={() => sortByUpvote()}>Most Upvotes</button>
            <button onClick={() => sortByDate()}></button>
        </div>
    )
}