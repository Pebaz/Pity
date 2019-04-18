function showItem(item)
{
	document.getElementById(item).classList.add('is-active');
}

function hideItem(item)
{
	document.getElementById(item).classList.remove('is-active');
}

function closeModal(item)
{
	var modal = document.getElementById(item);
	var modalCard = document.getElementById(item + '-card');

	var handler = function ()
	{
		console.log('DONE!');
		modal.classList.remove('fadeOut');
		modalCard.classList.remove('zoomOut');
		modal.removeEventListener('animationend', handler);
		hideItem(item);
	}

	modal.classList.add('fadeOut');
	modalCard.classList.add('zoomOut');
	modal.addEventListener('animationend', handler);
}
