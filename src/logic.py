import numpy as np
from collections import defaultdict


class Logic:

    def __init__(self):
        self.db = ''

    def borda_count(self, rankings, dislikes=None, top_n=1000):
        """
        Perform Borda Count aggregation on multiple ranked lists, considering dislikes.

        :param rankings: List of lists, where each sublist is a ranking of liked image IDs.
        :param dislikes: List of lists, where each sublist is a ranking of disliked image IDs.
        :param top_n: Number of top images to return.
        :return: List of image IDs sorted by aggregated Borda score.
        """
        scores = defaultdict(int)
        max_rank = max(len(r) for r in rankings) if rankings else 0  # Maximum rank across all lists
        max_dislike_rank = max(len(d) for d in dislikes) if dislikes else 0  # Max rank for dislikes

        # Process likes
        for ranking in rankings:
            for rank, image_id in enumerate(ranking):
                scores[image_id] += (max_rank - rank)  # Higher rank -> more points

        # Process dislikes (penalize)
        if dislikes:
            for dislike_ranking in dislikes:
                for rank, image_id in enumerate(dislike_ranking):
                    scores[image_id] -= (max_dislike_rank - rank)  # Higher rank -> more negative points

        # Sort images by total Borda score (higher is better)
        sorted_images = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return [image_id for image_id, _ in sorted_images[:top_n]]

    def get_similar_arts(self, liked_arts_ids, disliked_arts_ids, top_n=1000):

        set_ids = set(liked_arts_ids + disliked_arts_ids)

        liked_arts_embeddings, disliked_arts_embeddings = liked_arts_ids, disliked_arts_ids

        liked_similarity_lists = self.db.get_similarity_lists(liked_arts_embeddings)
        disliked_similarity_lists = self.db.get_similarity_lists(disliked_arts_embeddings)


        # extract them with the order by the ids
        liked_ranking = [result["entity"]["id"] for results_img in liked_similarity_lists for result in results_img[1:]]
        disliked_ranking = [result["entity"]["id"] for results_img in disliked_similarity_lists for result in results_img[1:]]

        similarity_list = self.borda_count(liked_ranking, disliked_ranking, top_n=top_n)
        similarity_list = [similar_id for similar_id in similarity_list if similar_id not in set_ids]

        return similarity_list