# Calculate IoU score

def IoU_scores(student_labels, solution_labels):
    IoU_scores = []

    for i in range(len(solution_labels)):
        student_array = decode_rle_to_mask(student_labels[i])
        ground_truth_array = decode_rle_to_mask(solution_labels[i])
        overlap = student_array * ground_truth_array # Logical AND
        union = student_array + ground_truth_array # Logical OR
        union[union>1] = 1
        IoU = overlap.sum()/float(union.sum())
        IoU_scores.append(IoU)

    return np.mean(IoU_scores)