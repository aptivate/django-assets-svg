function replace_svg_logo_with_png()
{
	var current_url = this.src;
	var png_url = current_url.substring(0, current_url.length - 4) + '.png';
	if (current_url.substring(0, current_url.length - 4) == '.svg')
	{
		this.src = png_url;
	}
}
