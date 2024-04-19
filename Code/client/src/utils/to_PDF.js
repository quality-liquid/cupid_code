export function to_pdf(content) {
    const {jsPDF} = window.jspdf;

    const doc = new jsPDF('p', 'pt', 'a4');
    console.log(doc)
    
    doc.html(content, {
        callback: function (doc) {
            doc.save("stats.pdf")
        },
        x: 400,
        y: 400
    })
    
}