# Hello World HTML Page

A simple, modern HTML page that displays "Hello World" with clean styling and interactive elements.

## Features

- **Clean Design**: Modern, gradient-based design with smooth animations
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive**: Includes a button that displays random messages
- **Accessible**: Follows web accessibility best practices
- **No Dependencies**: Pure HTML, CSS, and vanilla JavaScript

## Project Structure

```
.
├── index.html     # Main HTML page
├── style.css      # Stylesheet with modern design
└── README.md      # This file
```

## How to Use

### Option 1: Open Directly

Simply open `index.html` in any modern web browser:

```bash
# On macOS
open index.html

# On Linux
xdg-open index.html

# On Windows
start index.html
```

### Option 2: Use a Local Server

For a more realistic development environment, use a local web server:

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Then open http://localhost:8000 in your browser
```

**Using Node.js (with npx):**
```bash
npx http-server -p 8000

# Then open http://localhost:8000 in your browser
```

**Using PHP:**
```bash
php -S localhost:8000

# Then open http://localhost:8000 in your browser
```

## Features Breakdown

### HTML Structure
- Semantic HTML5 elements
- Proper meta tags for SEO and responsiveness
- Google Fonts integration (Inter font family)
- Accessible markup with ARIA considerations

### CSS Styling
- Modern gradient background
- Card-based layout with shadow effects
- Smooth animations and transitions
- Fully responsive design with mobile breakpoints
- Reduced motion support for accessibility
- Focus styles for keyboard navigation

### JavaScript Functionality
- Interactive button that displays random messages
- Auto-hide message after 3 seconds
- No external dependencies

## Browser Compatibility

This page works in all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

## Customization

You can easily customize the page:

1. **Change Colors**: Edit the gradient values in `style.css`
2. **Modify Text**: Update the content in `index.html`
3. **Add Messages**: Extend the `messages` array in the JavaScript section
4. **Adjust Layout**: Modify the card padding and sizing in `style.css`

## Learning Resources

- [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Web.dev - Learn Web Development](https://web.dev/learn/)

## License

This is a simple demonstration project. Feel free to use and modify as needed.
